# Datathon Passos Mágicos

<img width="29" height="39" alt="image" src="https://github.com/user-attachments/assets/c7c68151-ec02-4412-ac92-a413aca097c6" />  **Proposta:**

Esse estudo visa analisar os dados referemtes a notas escolares dos alunos da Passos Mágios entre os anos de 2022 e 2024 para identificar os diferentes impactos e probalidade de defasagem escolar. E assim, gerar insights estratégicos que apoiem a tomada de decisão e direcionamento gerencial na criação de medidas e padrões a serem adotados por profesores e time educacional em cenários que de turmas ou alunos com maiores desafios de aprendizado.

Em uma análise orientada por dados, que combina análise exploratória, engenharia de features temporais, modelagem preditiva e visualização interativa, esse estudo identifica e quantifica as interconexões entre características escolares, perfis sociodemográficos e vulnerabilidades econômicas, a fim de gerar um modelo direcionador de ações que permita que a Passos Mágicos faça uma triagem de alunos e posso criar planos de acompanhamento e comunicação estratégica para apoiar seus alunos.

O modelo desenvolvido não apenas identifica alunos em risco, mas também fornece insights sobre os fatores que mais influenciam a trajetória educacional, contribuindo para intervenções mais eficientes.

**• Engenharia de dados:** 

Após o processo de engenharia de dados, os registros foram unificados em um único dataset contendo aproximadamente:<br/>
•3030 registros<br/>
•24 variáveis principais<br/>
•3 anos de acompanhamento<br/><br/>


<img width="25" height="35" alt="image" src="https://github.com/user-attachments/assets/f6a95ab0-ed8d-4357-b1f5-f198503a997d" />  **A leitura completa do documento executivo pode ser feita aqui:**<BR/><BR/>

 <img width="25" height="35" alt="image" src="https://github.com/user-attachments/assets/291c7ccb-1da0-4e5e-a4e6-418759ad421d"/>   **Limitações do estudo:**
É importante ressaltar que os dados da PNAD COVID-19 são baseados em entrevistas domiciliares e autorrelato, não em prontuários médicos. Dessa forma, as conclusões refletem a percepção e o conhecimento dos entrevistados e não devem ser confundidas com dados clínicos de diagnóstico confirmado.

# Arquitetura


  **2. Principais indicadores educacionais**<BR/>
  •	Os indicadores presentes no dataset refletem diferentes dimensões do desenvolvimento do aluno. <br/>
 	
  **Indicador	Significado**
 	 •INDE	Índice de desempenho educacional geral
 	 •IAN	Adequação do nível educacional
   •IDA	Desempenho acadêmico
 	 •IEG	Engajamento nas atividades
 	 •IAA	Autoavaliação do aluno
 	 •IPS	Indicador psicossocial
 	 •IPP	Indicador psicopedagógico
 	 •IPV	Ponto de virada no desenvolvimento

Esses indicadores variam de 0 a 10, permitindo avaliar o desempenho e evolução dos estudantes ao longo do tempo.


# Engenharia de dados <br/>
Foi realizado um processo completo de data cleaning e padronização, pois o dataset apresentava diversos desafios,incluindo:
<BR/>
• O dataset original apresentava diversos desafios:
•	colunas inconsistentes entre anos;
•	valores ausentes;
•	formatação incorreta de algumas variáveis;
•	indicadores ausentes em determinados anos;
•	inconsistência no formato de datas;


**Padronização de colunas:**<BR/>
•	remoção de acentos
•	padronização de nomes
•	unificação de indicadores

**Tratamento de valores faltantes:**<BR/>
•	Em especial, o indicador IPP não existia no dataset de 2022.
Para resolver esse problema foi utilizado um método de imputação baseado em similaridade: 

**KNN Imputer:** Esse método estima valores ausentes com base em alunos semelhantes considerando os demais indicadores.






# Diagrama de tabela
![Imagem do WhatsApp de 2025-10-07 à(s) 15 10 16_3a476ae0](https://github.com/user-attachments/assets/0f569549-150d-4032-a0c3-777a33a41e73)

A tabela SOT possui 20 variáveis, distribuídas em grupos:<BR/>

• 4 variáveis de caracterização da pessoa (sexo, idade, escolaridade, cor ou raça).<BR/>
• 5 variáveis de sintomas clínicos da população (febre, tosse, dificuldade de respirar, fadiga, perda de olfato/paladar).<BR/>
• 3 variáveis de comportamento da população durante a pandemia (procurou atendimento, Pronto socorro SUS/UPA, Hospital do SUS, uso de hospital privado).<BR/>
• 3 variáveis econômicas (estava trabalhando, home office, rendimento bruto mensal efetivo, ).<BR/>
• 3 variáveis de partição (ano, mês, UF).
