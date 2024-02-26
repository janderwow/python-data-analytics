# simples
saldo = 1000;
saque = 200;
limite = 100;
conta_especial = True;

print(saldo);
print(saldo >= saque and saque <= limite);
print(saldo >= saque or saque <= limite);

print(saldo >= saque and saque <= limite) or (conta_especial and saldo >- saque);
print(not 1000 > 1500);

contatos_emergencia = [];

print(not contatos_emergencia);
