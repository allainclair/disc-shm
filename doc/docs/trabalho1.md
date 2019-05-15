Dada uma entrada em texto (.txt), código morse (.morse) ou áudio (.wav) a aplicação
deve usar essa entrada para traduzir para as outras duas
restantes.

Isto é, caso a entrada seja um texto, o programa deve escrever dois arquivos em
código morse (.morse) e sinal de áudio (.wav); caso seja um código morse, ela
deve escrever um arquivo de áudio (.wav) e um texto (.txt); caso a entrada seja
um áudio, a saída deve ser dois arquivos: texto (.txt) e código morse (.morse).

Pela extensão do arquivo de entrada, da pra saber quais arquivos de saída
devem ser gerados. Ex:

```Shell tab=
$ python app.py code.morse  # Gera arquivos text.txt e audio.wav
$ ./app.py audio.wav  # Gera arquivos text.txt e code.morse
```

Padronização de nomes: **app.py, text.txt, audio.wav e code.morse**

O arquivo de entrada fica livre para ter um nome qualquer, pois é um
parâmetro a ser passado para a aplicação.

## [Código Morse](https://en.wikipedia.org/wiki/Morse_code)

![mor-seimg](https://upload.wikimedia.org/wikipedia/commons/b/b5/International_Morse_Code.svg)

## 2 caracteres para codificação


* "0" e "1";
* "1" é uma unidade e nosso "ponto" (▄); 111 é o "traço" (▄▄▄);
* "0" significa os caracteres entre "pontos" e "traços", e tem quantidades
  de acordo com a especificação. Por exemplo: espaço entre letras tem apenas
  uma unidade, ou seja "0";
* Unidade de tempo de som como constante com valor de 0.25s. Isto é, uma
  unidade do código morse dura 0.25s, tratar uma pequena variação disso se for
  necessário, +- 0.01s;
* Frequência como constante 440 hz;
* Taxa de amostragem constante 48000;
* Amplitude 16000;
* [np.sin(2 * np.pi * frequency * x / sampling_rate) for x in range(num_samples)]

## Avaliação

* Completude;

* Qualidade de código:

    * Códigos claros;
    * Modularidade;
    * Nomes significativos;
    * Evitem códigos profundos (aninhados -- *nested*);
    * Evitem ultrapassar 80~90 caracteres por linha.

* Refatorem seus códigos para atingir esses objetivos!

* Testem o que for possível! Aconselho usar [TDD](
  https://en.wikipedia.org/wiki/Test-driven_development) em alguns casos!

    * Pytest;
    * Nose;
    * Unittest.
