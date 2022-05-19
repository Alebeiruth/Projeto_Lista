### Lista de Materias e Notas ###

materias = ["fisica", "calculo", "poesia", "historia"]
nota =[9.8, 9.7, 8.5, 8.8]
boletim = [["fisica", 9.8], ["calculo", 9.7], ["poesia", 8.5], ["historia", 8.8]]

boletim.append(["computacao", 10.0])
boletim.append(["artes", 9.3])
boletim[-1][-1] = 9.8
boletim[2].remove(8.5)
boletim[2].append("Passou")

semestre__extra_boletim = [["politica", 8.0], ["ingles", 9.6], ["musica", 9.7], ["redacao", 6.5]]
total_boletim = semestre__extra_boletim + boletim
print(total_boletim)
