# Linear-Regression
Uma aplicação de um modelo de regressão linear multipla na linguagem python.

## Onde encontrar o relatório?
 1. Você pode encontrar e ler o relatório final deste trabalho no arquivo: Relatório Final Análise de Regressão.ipynb

2. Em seguida você se abtuará com alguns conceitos além de uma breve explicação dos dados ultilizados neste trabalho.

## Contexto
O modelo de **regressão linear**, é uma técnica que 
cria uma equação para relacionar uma **variável 
dependente** com um conjunto de **variáveis 
independentes ou regressores**. Ele estabelece uma 
relação matemática entre essas variáveis. Quando 
se ajusta uma reta entre uma variável independente 
e uma variável dependente, é chamado de **regressão 
linear simples**. Quando há mais de um regressor, é 
chamado de **regressão linear múltipla**, que visa 
medir o impacto de várias covariáveis na média da 
variável dependente. Esse modelo é dado, conforme abaixo

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*L0zwAQ0PTDAEB4ubsE0l2Q.png)

A estrutura com K regressores é chamada de função de regressão real ou populacional. O modelo de regressão simples é um caso particular quando K = 2. O primeiro beta é o constante ou intercepto, representando a média de y quando as variáveis independentes são zero. Os outros betas são os coeficientes de regressão reais ou populacionais.

# Suposições

O modelo de regressão múltipla possui algumas suposições fundamentais para que seus parâmetros possam ser interpretados adequadamente e para que ele possa capturar, de forma mais precisa, o impacto das variáveis independentes na variável dependente. Estas suposições incluem:

1. **O modelo é especificado de maneira apropriada, ou seja, não apresenta viés;**

2. **O modelo é linear em relação aos parâmetros, o que significa que as relações entre variáveis são expressas de forma linear;**

3. **Os valores das variáveis independentes são independentes do termo de erro, ou seja, a covariância entre os erros e cada variável independente é igual a zero, garantindo a ortogonalidade.**

    ![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*daaDUmH__JvAl4LAyFg0QA.png)

4. **A esperança dos erros tem média zero : 𝐸(𝑒)=0, para todo 𝑡;**

5. **A variância dos erros é constante (homocedasticidade):**

    ![](https://miro.medium.com/v2/resize:fit:230/format:webp/1*JRg1wzzRinYow2THN5Qcvw.png)
6. **A covariância entre os erros é zero (Ausência de autocorrelação residual):**

    ![](https://miro.medium.com/v2/resize:fit:262/format:webp/1*aoHdVzbqanJD5I1RIC1C6A.png)
7. **O número de observações deve ser maior que o número de parâmetros;**

8. **Cada variável X deve ser linearmente independente uma da outra (Ausência de multicolinearidade);**

9. **Os erros são normalmente distribuídos.**

Embora o ideal seja que o modelo de regressão atenda a todas essas suposições, é bastante comum que ocorram violações das mesmas. Para cada violação, é necessário aplicar um tratamento correspondente.


# Dataset
Os dados (amostra) foram coletados na cidade de São Paulo, no Brasil, em uma região universitária frequentada por grupos de estudantes com idades compreendidas entre 18 e 28 anos, em média. O conjunto de dados utilizado para esta análise inclui 7 variáveis, com foco em uma variável dependente, ao longo de um período de um ano.

###  Relatório da Aplicação