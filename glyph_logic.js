const glyphMap = {
  1: "Seal",
  8: "Gate",
  99: "Return",
  111: "Signal Vector",
  222: "Resonance Chain",
  267: "Commerce",
  313: "Echo Twin",
  342: "Boundary",
  391: "Aftermark",
  494: "Folded Signal",
  555: "Time Thread",
  0: "🔄"
};

function decode() {
  const input = document.getElementById("sequence").value.trim().split(" ");
  let result = "";
  input.forEach(code => {
    const tag = glyphMap[parseInt(code)] || "[Unknown]";
    result += code + " → " + tag + "\n";
  });
  document.getElementById("output").innerText = result;
}

