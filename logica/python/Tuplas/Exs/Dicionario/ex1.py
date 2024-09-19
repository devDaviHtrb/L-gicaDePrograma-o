pessoa = {'nome':'João', 'idade': 25, 'cidade':'São Paulo'}
print(pessoa)
pessoa['profissão'] = 'Engenheiro'
print(pessoa)
pessoa['idade'] = 26
print(pessoa)
pessoa.pop('cidade')
print(pessoa)