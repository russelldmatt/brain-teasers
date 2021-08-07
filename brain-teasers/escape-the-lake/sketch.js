const V = p5.Vector;
console.log("loaded");

function circles(p5, radius, small_radius) {
  p5.strokeWeight(1);
  p5.stroke("black");
  p5.fill("#cce6ef");
  p5.ellipse(p5.width / 2, p5.height / 2, radius * 2, radius * 2);
  p5.noFill();
  p5.ellipse(p5.width / 2, p5.height / 2, small_radius * 2, small_radius * 2);
}

function naive(p5) {
  let v = 4;
  let dt = 1;
  let center, p, m, m_to_p;
  let radius = 200;
  let small_radius = radius / 4 - 2;

  p5.restart = () => {
    p = center;
    m = V.add(center, p5.createVector(radius, 0));
    m_to_p_fixed = undefined;
  };

  p5.setup = () => {
    p5.createCanvas(500, 500);
    p5.angleMode(p5.RADIANS);
    p5.textAlign(p5.CENTER, p5.CENTER);
    center = p5.createVector(p5.width / 2, p5.height / 2);
    m = V.add(center, p5.createVector(radius, 0));
    p = center;
    m_to_p = V.sub(center, m).normalize().mult(dt);
    circles(p5, radius, small_radius);
  };

  function within(x, y, tolerance) {
    return Math.abs(x - y) < tolerance;
  }

  p5.draw = () => {
    if (V.sub(p, center).mag() < radius) {
      p5.background("white");
      p5.noFill();
      p5.text(`v = ${v}`, p5.width - 50, 25);

      circles(p5, radius, small_radius);
      p5.strokeWeight(10);
      p5.stroke("red");
      p5.point(m.x, m.y);
      p5.stroke("blue");
      p5.point(p.x, p.y);

      p5.strokeWeight(1);
      p5.stroke("red");
      p5.line(center.x, center.y, m.x, m.y);
      p5.stroke("blue");
      p5.line(center.x, center.y, p.x, p.y);

      // text settings
      p5.strokeWeight(1);
      p5.stroke("black");
      p5.textSize(12);
      p5.fill(0);

      p = V.add(p, m_to_p);
      let p_ = V.sub(p, center);
      let m_ = V.sub(m, center);

      // figure out which way the monster wants to run
      let clockwise = V.rotate(m_, (v * dt) / radius);
      let counter = V.rotate(m_, (-v * dt) / radius);
      let dist_clockwise = V.sub(p_, clockwise).mag();
      let dist_counter = V.sub(p_, counter).mag();
      m_ = dist_counter < dist_clockwise ? counter : clockwise;
      m = V.add(center, m_);
    }
  };
}

function four(p5) {
  let v = 4;
  let dt = 1;
  let center, p, m;
  let radius = 200;
  let small_radius = radius / 4 - 2;
  let m_to_p_fixed;

  p5.restart = () => {
    p = center;
    m = V.add(center, p5.createVector(radius, 0));
    m_to_p_fixed = undefined;
  };

  p5.setup = () => {
    p5.createCanvas(500, 500);
    p5.angleMode(p5.RADIANS);
    p5.textAlign(p5.CENTER, p5.CENTER);
    center = p5.createVector(p5.width / 2, p5.height / 2);
    m = V.add(center, p5.createVector(radius, 0));
    p = center;
    circles(p5, radius, small_radius);
  };

  function within(x, y, tolerance) {
    return Math.abs(x - y) < tolerance;
  }

  p5.draw = () => {
    if (V.sub(p, center).mag() < radius) {
      p5.background("white");
      p5.noFill();
      p5.text(`v = ${v}`, p5.width - 50, 25);

      circles(p5, radius, small_radius);
      p5.strokeWeight(10);
      p5.stroke("red");
      p5.point(m.x, m.y);
      p5.stroke("blue");
      p5.point(p.x, p.y);

      p5.strokeWeight(1);
      p5.stroke("red");
      p5.line(center.x, center.y, m.x, m.y);
      p5.stroke("blue");
      p5.line(center.x, center.y, p.x, p.y);

      // text settings
      p5.strokeWeight(1);
      p5.stroke("black");
      p5.textSize(12);
      p5.fill(0);

      let p_ = V.sub(p, center);
      let m_ = V.sub(m, center);
      let p_dist = p_.mag();
      let p_heading = p_.heading();
      let m_heading = m_.heading();
      let m_to_p = V.sub(p_, m_).normalize().mult(dt);
      let eps = 1;
      // if p is within the small circle, get to the outside first
      if (p_dist < small_radius - eps) {
        p = V.add(p, m_to_p);
      } else if (within(p_dist, small_radius, eps) && !m_to_p_fixed) {
        p5.text("circle...", center.x, center.y);
        let heading_diff =
          (p_heading - m_heading + 2 * Math.PI) % (2 * Math.PI);
        if (within(heading_diff, Math.PI, 0.02)) {
          // you're now directly opposite the monster, RUN!
          m_to_p_fixed = m_to_p;
          p = V.add(p, m_to_p_fixed);
          p5.print("RUN!");
        } else {
          // run in a circle until you're directly opposite the monster
          p = V.add(center, V.rotate(p_, dt / small_radius));
        }
      } else {
        p5.text("RUN!", center.x, center.y);
        p = V.add(p, m_to_p_fixed);
      }

      // figure out which way the monster wants to run
      let clockwise = V.rotate(m_, (v * dt) / radius);
      let counter = V.rotate(m_, (-v * dt) / radius);
      let dist_clockwise = V.sub(p_, clockwise).mag();
      let dist_counter = V.sub(p_, counter).mag();
      m_ = dist_counter < dist_clockwise ? counter : clockwise;
      m = V.add(center, m_);
    }
  };
}

function optimal(p5) {
  let v = 4.55;
  let dt = 1;
  let center, p, m;
  let radius = 200;
  let small_radius = radius / v - 2;
  let m_to_p_fixed;

  p5.restart = () => {
    p = center;
    m = V.add(center, p5.createVector(radius, 0));
    m_to_p_fixed = undefined;
  };

  p5.setup = () => {
    p5.createCanvas(500, 500);
    p5.angleMode(p5.RADIANS);
    p5.textAlign(p5.CENTER, p5.CENTER);
    center = p5.createVector(p5.width / 2, p5.height / 2);
    m = V.add(center, p5.createVector(radius, 0));
    p = center;
    circles(p5, radius, small_radius);
  };

  function within(x, y, tolerance) {
    return Math.abs(x - y) < tolerance;
  }

  p5.draw = () => {
    if (V.sub(p, center).mag() < radius) {
      p5.background("white");
      p5.noFill();
      p5.text(`v = ${v}`, p5.width - 50, 25);

      circles(p5, radius, small_radius);
      p5.strokeWeight(10);
      p5.stroke("red");
      p5.point(m.x, m.y);
      p5.stroke("blue");
      p5.point(p.x, p.y);

      p5.strokeWeight(1);
      p5.stroke("red");
      p5.stroke("blue");

      // text settings
      p5.strokeWeight(1);
      p5.stroke("black");
      p5.textSize(12);
      p5.fill(0);

      let p_ = V.sub(p, center);
      let m_ = V.sub(m, center);
      let p_dist = p_.mag();
      let p_heading = p_.heading();
      let m_heading = m_.heading();
      let m_to_p = V.sub(p_, m_).normalize().mult(dt);
      let eps = 1;
      // if p is within the small circle, get to the outside first
      if (p_dist < small_radius - eps) {
        p = V.add(p, m_to_p);
      } else if (within(p_dist, small_radius, eps) && !m_to_p_fixed) {
        p5.text("circle...", center.x, center.y);
        let heading_diff =
          (p_heading - m_heading + 2 * Math.PI) % (2 * Math.PI);
        if (within(heading_diff, Math.PI, 0.02)) {
          // you're now directly opposite the monster, RUN!
          m_to_p_fixed = V.rotate(m_to_p, Math.PI / 2);
          p = V.add(p, m_to_p_fixed);
          p5.print("RUN!");
        } else {
          // run in a circle until you're directly opposite the monster
          p = V.add(center, V.rotate(p_, dt / small_radius));
        }
      } else {
        p5.text("RUN!", center.x, center.y);
        p = V.add(p, m_to_p_fixed);
      }

      // figure out which way the monster wants to run
      let clockwise = V.rotate(m_, (v * dt) / radius);
      let counter = V.rotate(m_, (-v * dt) / radius);
      let dist_clockwise = V.sub(p_, clockwise).mag();
      let dist_counter = V.sub(p_, counter).mag();
      m_ = dist_counter < dist_clockwise ? counter : clockwise;
      m = V.add(center, m_);
    }
  };
}
