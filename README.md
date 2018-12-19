# Marcador-placar-Petrobowl
Petrobowl é uma competição internacional de conhecimentos na área de petróleo e gás, para as rodadas de treino da equipe da UFAM, foi desenvolvido um placar simples em python que automatizou o processo.

## Como funciona o campeonato?
Nesta competição, existem as toss-up question e as bonus questions. Cada equipe tem 5 segundos para apertar o buzzer e responder a toss-up, quem acertar recebe uma quantidade de pontos, porém se errar, os pontos são subtraídos do total da equipe.

Se a equipe acertar a toss-up, tem direito a uma bonus questions, nesta etapa, se errar, não perde pontos.

## Entendendo o programa
O programa feito em python tem como entradas principais qual equipe acertou (1, 2 ou 0, sendo 0 atribuido caso nenhum equipe acerte), em seguida é perguntado a quantidade de pontos que esta equipe recebeu _**ou**_ perdeu (-), em seguida se pergunta o mesmo em relação a questão bonus (também pode ser atribuído 0 caso não acerte). Ao final de cada rodada é exibido o placar atual e o contador de rodadas atualiza.

**OBS.:** Para repassar o programa funcional para que todos da equipe pudessem usar, criou-se um `.exe` utilizando `pyinstaller`, dessa maneira, a última linha contém um input para o prompt só fechar após todos conseguirem ver o resultado final e apertarem enter.
