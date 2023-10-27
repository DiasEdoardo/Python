idade = int(input('Qual a sua idade?\n'));
if idade == 16 or idade == 17 or idade >=70:
    print('seu voto é facultativo');
elif idade >= 18 and idade <70:
    print('o seu voto é obrigatorio');
else:
    print('voce nao pode votar');