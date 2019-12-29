Jogo original:
http://www.bpixel.com.br/cursos/cannonlord/

O que encontrar no projeto
----------------------------

Os projeto possuem uma pasta denominada "CannonLord" onde se encontra as pasta Anim, Objetos, Scripts e Imagens,
onde sao respectivamente encontrado as animacoes, objetos, scripts e imagens utilizados para criar o jogo.
No desenvolvimento dos script foi utilizado puramente a linguagem em C#.
No codigo tentei deixar os nomes das variaveis e dos metodos o mais proximo possivel da finalidade deles.
Partes em que vi que possuia um conteudo extenso separei e coloquei em outro metodo, exemplo: 
estrutura extensa de if e else.
Nao utilizei de muitos comentarios no codigo devido ao nome estar proximo de sua finalidade.

Relatorio adicional
----------------------
Iniciei o desenvolvimento do designer do jogo na terca - feira, terminando o desenvolvimento mais proximo possivel 
do jogo original no dia seguinte quarta - feira.
Comecei assim, a programacao dos scripts do jogo no mesmo dia por volta das 15 horas.
Optei por comecar a fazer o movimento giratorio do canhao de se movimentar para um lado e para o outro e seus tiro.
Obter exito em fazer o canhao girar foi facil ja que decidir utilizar o eixo de rotacao Z da unity, demorei um pouco
para descobri como disparar um tiro da ponta do canhao, apos isto, desenvolvi a colisao da bala com os obstaculos. 
No dia seguinte quinta - feira fiz a inteligencia artificial, poderia ter utilizado o animation da propria unity
para fazer esta parte, mas nao encontrei a opcao "Sample" para modificar a velocidade de reproducao e gravacao do aniamtion,
entao, desenvolvi uma IA via script, deu um pouco de dor de cabeca ja que demorei quase que o dia todo para descobrir que no
script eu tinha que utiliza um "*(-1)" no eixo y, mas superado mais um desafio e consegui avancar, assim, la estava eu
na reta final para o desenvolvimento da v1.0, entao, no finalzinho do dia consegui terminar o restante do script: 
botoes, quadro, pontos e morte dos inimigos, tentei deixar o alinhamento e tamanho do texto dos botoes de uma maneira
visualizavel e clicavel, mas, acredito que nao obtive tanto sucesso assim. Mas, na minha visao ficou ao menos de uma maneira
jogavel.
Na sexta - feira, iniciei o desenvolvimento da v2.0 do jogo que seria uma modificacao de como o jogo poderia ser melhor,
como me restava 2 dias para entrega do projeto com o prazo preferencial de 1 semana contado a partir de domingo, sem
habilidade nenhuma com designer e com muito pouco conhecimento em particulas para fazer algo realmente bom. Optei, por
reutilizar as imagens que me foram fornecidas, assim, mudei a cor do morcego e do tiro, aumentando um pouco o tamanho do tiro,
para da uma diferenciada. No sabado criei um script para da 2 pontos de vida para o novo morcego, e um botao especial para 
disparar o novo projetil e assim limpar o mapa desses terriveis morcegos.

Terminando dei build para as 3 plataforma que me foram pedido: windows, android e webgl.
o webgl foi o unico que nao consegui utilizar por erro na durante da propria unity,por algum motivo só funcionava quando
o mesmo criava dominio artificial (um localhost:6556, por exemplo). Segue o anexo do web v1.0:

Jogo
--------
https://eversoncordeirosilva.github.io/CannonMasterWeb_v1/

Repositorio
-----------------
https://github.com/EversonCordeiroSilva/CannonMasterWeb_v1
