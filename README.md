# Datathon Passos Mágicos ✨👣

<img width="29" height="39" alt="image" src="https://github.com/user-attachments/assets/c7c68151-ec02-4412-ac92-a413aca097c6" />  **Proposta:**

Esse estudo visa analisar os dados referemtes a notas escolares dos alunos da Passos Mágios entre os anos de 2022 e 2024 para identificar os diferentes impactos e probalidade de defasagem escolar. E assim, gerar insights estratégicos que apoiem a tomada de decisão e direcionamento gerencial na criação de medidas e padrões a serem adotados por profesores e time educacional em cenários que de turmas ou alunos com maiores desafios de aprendizado.

Em uma análise orientada por dados, que combina análise exploratória, engenharia de features temporais, modelagem preditiva e visualização interativa, esse estudo identifica e quantifica as interconexões entre características escolares, perfis sociodemográficos e vulnerabilidades econômicas, a fim de gerar um modelo direcionador de ações que permita que a Passos Mágicos faça uma triagem de alunos e posso criar planos de acompanhamento e comunicação estratégica para apoiar seus alunos.

O modelo desenvolvido não apenas identifica alunos em risco, mas também fornece insights sobre os fatores que mais influenciam a trajetória educacional, contribuindo para intervenções mais eficientes.


<img width="25" height="35" alt="image" src="https://github.com/user-attachments/assets/f6a95ab0-ed8d-4357-b1f5-f198503a997d" />  **A leitura completa do documento executivo pode ser feita no arquivo disponivel no repositório**<BR/><BR/>


# Arquitetura
<BR/>
Após o processo de engenharia de dados, os registros foram unificados em um único dataset contendo aproximadamente:

<BR/> •3030 registros<br/>
<BR/> •24 variáveis principais<br/>
<BR/> •3 anos de acompanhamento<BR/><BR/>

 <img width="24" height="25" alt="image" src="https://github.com/user-attachments/assets/2fbdd06f-5f36-4eda-b842-0549ba87a515" />   **Principais indicadores educacionais**<BR/>
  Os indicadores presentes no dataset refletem diferentes dimensões do desenvolvimento do aluno. <br/>
 	
  **Indicador	e seu significado:**
 	<BR/> •INDE = 	Índice de desempenho educacional geral
 <BR/>	 •IAN =	Adequação do nível educacional
<BR/>   •IDA	= Desempenho acadêmico
<BR/> 	 •IEG = 	Engajamento nas atividades
 <BR/>	 •IAA = 	Autoavaliação do aluno
<BR/> 	 •IPS	= Indicador psicossocial
<BR/> 	 •IPP = 	Indicador psicopedagógico
 <BR/>	 •IPV =	Ponto de virada no desenvolvimento

<BR/> Esses indicadores variam de 0 a 10, permitindo avaliar o desempenho e evolução dos estudantes ao longo do tempo.

<BR/>
<img width="24" height="25" alt="image" src="https://github.com/user-attachments/assets/e93cf9f3-d96d-48a7-b5ce-bf412b487893" /> Engenharia de dados:
<BR/> Foi realizado um processo completo de data cleaning e padronização, pois o dataset apresentava diversos desafios, incluindo:
<BR/>
<BR/> • O dataset original apresentava diversos desafios:
<BR/> •	colunas inconsistentes entre anos;
<BR/> •	valores ausentes;
<BR/> •	formatação incorreta de algumas variáveis;
<BR/> •	indicadores ausentes em determinados anos;
<BR/> •	inconsistência no formato de datas;

<BR/>
<BR/> <img width="24" height="25" alt="image" src="https://github.com/user-attachments/assets/3beb991f-30b9-430b-9043-1094085845b2" /> Padronização de colunas:

<BR/> •	remoção de acentos
<BR/> • padronização de nomes
<BR/> •	unificação de indicadores
<BR/>

<BR/><BR/> <img width="24" height="25" alt="image" src="https://github.com/user-attachments/assets/daf6479c-e05c-4b96-a515-e27d185bd187" /> **Tratamento de valores faltantes:** <BR/>
<BR/>•	Em especial, o indicador IPP não existia no dataset de 2022.
Para resolver esse problema foi utilizado um método de imputação baseado em similaridade: 

<BR/>**KNN Imputer:** Esse método estima valores ausentes com base em alunos semelhantes considerando os demais indicadores.

<BR/>
<img width="24" height="25" alt="image" src="https://github.com/user-attachments/assets/f11de075-b161-4b74-a07f-665beaa8b927" /> Engenharia de Features:
<BR/>
Para melhorar o desempenho do modelo foram criadas features temporais, que capturam a evolução do aluno ao longo dos anos.
Tempo no programa, sendo elas: 

<BR/><BR/><img width="24" height="24" alt="image" src="https://github.com/user-attachments/assets/a9d08294-a9ea-4b84-9eb7-cec9203d0ad8" /> **Tempo de programa**
<BR/> • TEMPO_PROGRAMA = ANO_ATUAL - ANO_INGRESSO<BR/><BR/>
Essa variável mede o tempo de permanência do aluno no programa.<BR/>

<BR/><img width="24" height="24" alt="image" src="https://github.com/user-attachments/assets/a9d08294-a9ea-4b84-9eb7-cec9203d0ad8" /> **Repetência de fase**
<BR/> •REPETENTE_FASE<BR/>
Uma variável binária indicando se o aluno permaneceu na mesma fase por mais de um ano.<BR/>
Isso permite capturar possíveis dificuldades de progressão no programa.<BR/>

<BR/>
<BR/><img width="24" height="24" alt="image" src="https://github.com/user-attachments/assets/a9d08294-a9ea-4b84-9eb7-cec9203d0ad8" /> Variação anual dos indicadores
<BR/>Além disso, as mudanças nos indicadores entre anos consecutivos foram calculadas.
<BR/>Exemplo:
<BR/>
<BR/>•	DELTA_IDA
<BR/>•	DELTA_IEG
<BR/>•	DELTA_IAA
<BR/>•	DELTA_IPS
<BR/>•	DELTA_IPP
<BR/>•	DELTA_IPV
<BR/><BR/>
Essas variáveis capturam tendências de melhora ou deterioração no desempenho do aluno.








