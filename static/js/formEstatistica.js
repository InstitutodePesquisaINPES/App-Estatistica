const form = document.getElementById("form");

// Adicione IDs únicos para cada input no HTML e altere aqui para correspondência
const nome_cidade = document.getElementById("nome_cidade");
const populacao = document.getElementById("populacao");
const porte_cidade = document.getElementById("porte_cidade");
const porte_inferior = document.getElementById("porte_inferior");
const porte_superior = document.getElementById("porte_superior");
const distancia = document.getElementById("distancia");
const qnt_bairros = document.getElementById("qnt_bairros");
const qnt_rurais = document.getElementById("qnt_rurais");
const eleitorado = document.getElementById("eleitorado");
const nvl_confianca = document.getElementById("nvl_confianca");
const margem_erro = document.getElementById("margem_erro");
const tipo_pesquisa = document.getElementById("tipo_pesquisa");
const qnt_perguntas = document.getElementById("qnt_perguntas");
const ambpg = document.getElementById("ambpg");
const ambeg = document.getElementById("ambeg");
const ambps = document.getElementById("ambps");
const ambes = document.getElementById("ambes");
const vp_bps = document.getElementById("vp_bps");
const vp_bes = document.getElementById("vp_bes");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  checkInputs();
});

function checkInputs() {
  // Obtenha os valores dos inputs
  const nome_cidadeValue = nome_cidade.value;
  const populacaoValue = populacao.value;
  const porte_cidadeValue = porte_cidade.value;
  const porte_inferiorValue = porte_inferior.value;
  const porte_superiorValue = porte_superior.value;
  const distanciaValue = distancia.value;
  const qnt_bairrosValue = qnt_bairros.value;
  const qnt_ruraisValue = qnt_rurais.value;
  const eleitoradoValue = eleitorado.value;
  const nvl_confiancaValue = nvl_confianca.value;
  const margem_erroValue = margem_erro.value;
  const tipo_pesquisaValue = tipo_pesquisa.value;
  const qnt_perguntasValue = qnt_perguntas.value;
  const ambpgValue = ambpg.value;
  const ambegValue = ambeg.value;
  const ambpsValue = ambps.value;
  const ambesValue = ambes.value;
  const vp_bpsValue = vp_bps.value;
  const vp_besValue = vp_bes.value;


  // Exemplo de verificação simples para o nome da cidade
  if (nome_cidadeValue === "") {
    setErrorFor(nome_cidade, "O nome da cidade é obrigatório.");
  } else {
    setSuccessFor(nome_cidade);
  }

  // Exemplo de verificação para o AMBPG
  if (ambpgValue === "") {
    setErrorFor(ambpg, "Informe o valor estimado para o AMBPG.");
  } else {
    setSuccessFor(ambpg);
  }


  // Verificação final de validade do formulário
  const formControls = form.querySelectorAll(".form-control");

  const formIsValid = [...formControls].every((formControl) => {
    return formControl.className === "form-control success";
  });

  if (formIsValid) {
    console.log("O formulário está 100% válido!");
  }
}

// Exemplo de função setErrorFor
function setErrorFor(input, message) {
  const formControl = input.parentElement;
  const small = formControl.querySelector("small");

  // Adiciona a mensagem de erro
  small.innerText = message;

  // Adiciona a classe de erro
  formControl.className = "form-control error";
}

// Exemplo de função setSuccessFor
function setSuccessFor(input) {
  const formControl = input.parentElement;

  // Adicionar a classe de sucesso
  formControl.className = "form-control success";
}
