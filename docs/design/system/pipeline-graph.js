/* Pipeline graph: Rahzaan's LangGraph topology drawn in WebGL, no library.
   Decorative. The canvas is aria-hidden and every fact it shows is in the
   figure caption as text (DESIGN.md hard limit 1).

   Topology: 24 nodes and the edges between them, read from the graph
   definition in Rahzaan's backend on 2026-10-03. Nodes are anonymous here:
   indices only, no names, so nothing private leaves that repository.
   Layer is the node's depth along its longest path from START, except node
   22, which hangs off the dispatcher but is drawn beside node 21 because
   both feed the final node.

   Cost controls, each because of ADR-0009:
   - starts only after the load event, when the browser is idle, so it can
     never delay the largest paint;
   - draws nothing while off screen or while the tab is hidden;
   - under prefers-reduced-motion it draws one still frame and stops;
   - device pixel ratio capped at 2. */
(function () {
  var LAYERS = [0,0,0,0,0,0,0,0,0, 1, 2,2,2,2, 3, 4, 3, 5,5,5, 6, 7, 7, 8];
  var EDGES = [
    [0,9],[1,9],[2,9],[3,9],[4,9],[5,9],[6,9],[7,9],[8,9],
    [9,10],[9,11],[9,12],[9,13],[9,22],
    [12,14],[13,14],[14,15],[11,16],
    [15,17],[15,18],[15,19],[17,20],
    [20,21],[18,21],[19,21],[16,21],[6,21],[10,21],
    [21,23],[22,23]
  ];
  var N = LAYERS.length, DEPTH = 8;

  function positions() {
    var byLayer = {}, out = new Float32Array(N * 3);
    LAYERS.forEach(function (l, i) { (byLayer[l] = byLayer[l] || []).push(i); });
    Object.keys(byLayer).forEach(function (l) {
      var ids = byLayer[l], n = ids.length;
      var r = n === 1 ? 0 : 0.22 + 0.075 * n;
      ids.forEach(function (id, k) {
        var a = (k / n) * Math.PI * 2 + l * 0.7;
        out[id * 3] = (l / DEPTH) * 3.4 - 1.7;
        out[id * 3 + 1] = Math.cos(a) * r;
        out[id * 3 + 2] = Math.sin(a) * r;
      });
    });
    return out;
  }

  var VS = [
    'attribute vec3 p; attribute float s; uniform mat4 m; uniform float px;',
    'varying float v;',
    'void main(){ vec4 q = m * vec4(p,1.0); gl_Position = q;',
    ' gl_PointSize = px * (0.6 + s) / q.w; v = s; }'].join('\n');
  var FS_POINT = [
    'precision mediump float; uniform vec3 c; uniform vec3 hi; varying float v;',
    'void main(){ vec2 d = gl_PointCoord - 0.5; float r = length(d);',
    ' float a = 1.0 - smoothstep(0.42, 0.5, r); if (a <= 0.0) discard;',
    ' gl_FragColor = vec4(mix(c, hi, clamp(v, 0.0, 1.0)) * a, a); }'].join('\n');
  var FS_LINE = [
    'precision mediump float; uniform vec3 c; uniform float alpha;',
    'void main(){ gl_FragColor = vec4(c * alpha, alpha); }'].join('\n');

  function hexToRgb(h) {
    h = (h || '').trim().replace('#', '');
    if (h.length === 3) h = h.split('').map(function (x) { return x + x; }).join('');
    var n = parseInt(h, 16);
    if (isNaN(n)) return [0.5, 0.5, 0.5];
    return [(n >> 16 & 255) / 255, (n >> 8 & 255) / 255, (n & 255) / 255];
  }

  function perspective(f, aspect, near, far) {
    var t = 1 / Math.tan(f / 2), nf = 1 / (near - far);
    return [t / aspect,0,0,0, 0,t,0,0, 0,0,(far+near)*nf,-1, 0,0,2*far*near*nf,0];
  }
  function mul(a, b) {
    var o = new Array(16);
    for (var i = 0; i < 4; i++) for (var j = 0; j < 4; j++) {
      var s = 0; for (var k = 0; k < 4; k++) s += a[k * 4 + j] * b[i * 4 + k];
      o[i * 4 + j] = s;
    }
    return o;
  }
  function rotX(t) { var c = Math.cos(t), s = Math.sin(t); return [1,0,0,0, 0,c,s,0, 0,-s,c,0, 0,0,0,1]; }
  function rotY(t) { var c = Math.cos(t), s = Math.sin(t); return [c,0,-s,0, 0,1,0,0, s,0,c,0, 0,0,0,1]; }
  function trans(z) { return [1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,z,1]; }

  function start(canvas) {
    var gl = canvas.getContext('webgl', { antialias: true, premultipliedAlpha: true, alpha: true, powerPreference: 'low-power' });
    if (!gl) { canvas.hidden = true; return; }
    canvas.closest('figure') && canvas.closest('figure').classList.add('graph--live');

    function prog(fs) {
      var p = gl.createProgram();
      [[gl.VERTEX_SHADER, VS], [gl.FRAGMENT_SHADER, fs]].forEach(function (x) {
        var sh = gl.createShader(x[0]); gl.shaderSource(sh, x[1]); gl.compileShader(sh); gl.attachShader(p, sh);
      });
      gl.linkProgram(p); return p;
    }
    var pp = prog(FS_POINT), lp = prog(FS_LINE);
    var pos = positions();

    var lineVerts = new Float32Array(EDGES.length * 6);
    EDGES.forEach(function (e, i) {
      for (var k = 0; k < 3; k++) { lineVerts[i*6+k] = pos[e[0]*3+k]; lineVerts[i*6+3+k] = pos[e[1]*3+k]; }
    });
    var bLine = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, bLine); gl.bufferData(gl.ARRAY_BUFFER, lineVerts, gl.STATIC_DRAW);
    var bNode = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, bNode); gl.bufferData(gl.ARRAY_BUFFER, pos, gl.STATIC_DRAW);
    var nodeGlow = new Float32Array(N), bGlow = gl.createBuffer();
    var pulse = new Float32Array(EDGES.length * 3), pulseS = new Float32Array(EDGES.length);
    var bPulse = gl.createBuffer(), bPulseS = gl.createBuffer();
    var zero = new Float32Array(EDGES.length * 2), bZero = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, bZero); gl.bufferData(gl.ARRAY_BUFFER, zero, gl.STATIC_DRAW);

    var colours = {};
    function readColours() {
      var cs = getComputedStyle(canvas);
      colours.node = hexToRgb(cs.getPropertyValue('--ink'));
      colours.hi = hexToRgb(cs.getPropertyValue('--accent'));
      colours.line = hexToRgb(cs.getPropertyValue('--rule-strong'));
    }
    readColours();

    var w = 0, h = 0;
    function size() {
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      var r = canvas.getBoundingClientRect();
      w = Math.max(1, Math.round(r.width * dpr)); h = Math.max(1, Math.round(r.height * dpr));
      if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; }
      gl.viewport(0, 0, w, h);
    }

    function attrib(p, name, buf, n) {
      var loc = gl.getAttribLocation(p, name);
      if (loc < 0) return;
      gl.bindBuffer(gl.ARRAY_BUFFER, buf); gl.enableVertexAttribArray(loc);
      gl.vertexAttribPointer(loc, n, gl.FLOAT, false, 0, 0);
    }

    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
    var visible = false, raf = 0, t0 = -1, PERIOD = 7000, last = 0;
    /* 30 frames a second, and two passes of the wave, then it rests on a
       still frame. Measured cost of running it unbounded: see README. */
    var RUN_MS = PERIOD * 2, FRAME_MS = 1000 / 30;
    var U = function (p, n) { return (p.u = p.u || {})[n] || (p.u[n] = gl.getUniformLocation(p, n)); };

    function frame(now) {
      raf = 0;
      if (t0 < 0) t0 = now;
      if (!reduce.matches && now - t0 < RUN_MS && now - last < FRAME_MS - 1) { raf = requestAnimationFrame(frame); return; }
      last = now;
      size();
      var still = reduce.matches || now - t0 >= RUN_MS;
      var t = reduce.matches ? 0 : Math.min(now - t0, RUN_MS) / 1000;
      var phase = still ? -1 : ((now - t0) % PERIOD) / PERIOD * (DEPTH + 1.5) - 0.5;

      for (var i = 0; i < N; i++) {
        var d = Math.abs(phase - LAYERS[i]);
        nodeGlow[i] = still ? 0.15 : Math.max(0, 1 - d * 1.6);
      }
      var np = 0;
      EDGES.forEach(function (e, i) {
        var a = LAYERS[e[0]], b = LAYERS[e[1]];
        var u = (phase - a) / Math.max(1, b - a);
        if (!still && u > 0 && u < 1) {
          for (var k = 0; k < 3; k++) pulse[np*3+k] = pos[e[0]*3+k] + (pos[e[1]*3+k] - pos[e[0]*3+k]) * u;
          pulseS[np] = 0.9; np++;
        }
      });

      var aspect = w / h;
      var m = mul(perspective(0.62, aspect, 0.1, 20), mul(trans(-3.9), mul(rotY(-0.36), rotX(0.35 + t * 0.12))));
      if (aspect < 1.6) m = mul(perspective(0.62, aspect, 0.1, 20), mul(trans(-6.4), mul(rotY(-0.36), rotX(0.35 + t * 0.12))));

      gl.clearColor(0, 0, 0, 0); gl.clear(gl.COLOR_BUFFER_BIT);
      gl.enable(gl.BLEND); gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);

      gl.useProgram(lp);
      gl.uniformMatrix4fv(U(lp, 'm'), false, m);
      gl.uniform3fv(U(lp, 'c'), colours.line);
      gl.uniform1f(U(lp, 'alpha'), 0.85);
      gl.uniform1f(U(lp, 'px'), 0);
      attrib(lp, 'p', bLine, 3); attrib(lp, 's', bZero, 1);
      gl.drawArrays(gl.LINES, 0, EDGES.length * 2);

      gl.useProgram(pp);
      gl.uniformMatrix4fv(U(pp, 'm'), false, m);
      gl.uniform3fv(U(pp, 'c'), colours.node);
      gl.uniform3fv(U(pp, 'hi'), colours.hi);
      gl.uniform1f(U(pp, 'px'), 58 * Math.min(window.devicePixelRatio || 1, 2));
      gl.bindBuffer(gl.ARRAY_BUFFER, bGlow); gl.bufferData(gl.ARRAY_BUFFER, nodeGlow, gl.DYNAMIC_DRAW);
      attrib(pp, 'p', bNode, 3); attrib(pp, 's', bGlow, 1);
      gl.drawArrays(gl.POINTS, 0, N);

      if (np) {
        gl.bindBuffer(gl.ARRAY_BUFFER, bPulse); gl.bufferData(gl.ARRAY_BUFFER, pulse.subarray(0, np * 3), gl.DYNAMIC_DRAW);
        gl.bindBuffer(gl.ARRAY_BUFFER, bPulseS); gl.bufferData(gl.ARRAY_BUFFER, pulseS.subarray(0, np), gl.DYNAMIC_DRAW);
        gl.uniform1f(U(pp, 'px'), 30 * Math.min(window.devicePixelRatio || 1, 2));
        attrib(pp, 'p', bPulse, 3); attrib(pp, 's', bPulseS, 1);
        gl.drawArrays(gl.POINTS, 0, np);
      }
      if (!still && visible && !document.hidden) raf = requestAnimationFrame(frame);
    }
    function kick() { if (!raf) raf = requestAnimationFrame(frame); }

    if (!('IntersectionObserver' in window)) visible = true;
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) { visible = es[0].isIntersecting; if (visible) kick(); }).observe(canvas);
    }
    document.addEventListener('visibilitychange', function () { if (!document.hidden) kick(); });
    reduce.addEventListener && reduce.addEventListener('change', kick);
    window.addEventListener('resize', kick);
    var themeChange = function () { readColours(); kick(); };
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', themeChange);
    new MutationObserver(themeChange).observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme', 'class'] });
    kick();
  }

  function boot() {
    var go = function () { document.querySelectorAll('canvas[data-pipeline-graph]').forEach(start); };
    if ('requestIdleCallback' in window) requestIdleCallback(go, { timeout: 1500 }); else setTimeout(go, 200);
  }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot, { once: true });
})();
