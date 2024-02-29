larg = float(input('largura da parede:'))
alt = float(input('altura da parede:'))
area = larg * alt 
print('Sua parede com a dimensão de {}x{} e sua area de {}M²'.format(larg, alt, area))
tinta = area/2
print('para pintar essa parede, você precisar[a de {}L de tinta'.format(tinta))