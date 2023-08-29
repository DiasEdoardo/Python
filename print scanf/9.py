totaleleitores = int(input('qual o numero total de eleitores do seu municipio?\n'));
brancos = int(input('qual a quantidade de votos brancos?\n'));
nulos = int(input('qual a quantidade de votos nulos?\n'));
validos = int(input('qual a quantidade de votos validos?\n'));
pb=brancos/totaleleitores*100;
pn=nulos/totaleleitores*100;
pv=validos/totaleleitores*100;
print('o percentual de votos brancos é',pb,'\no percentual de votos nulos é ',pn,'\ne o percentual de votos validos é',pv);
