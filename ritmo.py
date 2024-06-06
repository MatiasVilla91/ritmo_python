from music21 import stream, midi, note, tempo


def generar_ritmo_bateria(duracion_compases=4, bpm=220, archivo='220.mid'):
    ritmo = stream.Stream()
    ritmo.append(tempo.MetronomeMark(number=bpm))

    for compas in range(duracion_compases):
        for i in range(4):
            # Agregar hi-hat en cada tiempo
            hihat = note.Note("F#2", quarterLength=1)
            ritmo.append(hihat)

            if i % 4 == 0:
                # Bombo en el tiempo 1
                kick = note.Note("C2", quarterLength=1)
                ritmo.append(kick)
            elif i % 4 == 1:
                # Caja en el tiempo 2
                snare = note.Note("D2", quarterLength=1)
                ritmo.append(snare)
            elif i % 4 == 2:
                # Bombo en el tiempo 3
                kick = note.Note("C2", quarterLength=1)
                ritmo.append(kick)
            elif i % 4 == 3:
                # Caja en el tiempo 4
                snare = note.Note("D2", quarterLength=1)
                ritmo.append(snare)

        # Agregar un corte al final del compás
        if compas == duracion_compases - 1:
            ritmo.append(note.Note("C2", quarterLength=0.5))  # Bombo
            ritmo.append(note.Note("D2", quarterLength=0.5))  # Caja
            ritmo.append(note.Note("C2", quarterLength=0.5))  # Bombo
            ritmo.append(note.Note("D2", quarterLength=0.5))  # Caja
            ritmo.append(note.Note("D2", quarterLength=0.5))  # Caja
            ritmo.append(note.Note("D2", quarterLength=0.5))  # Caja
            ritmo.append(note.Note("D2", quarterLength=0.5))  # Caja

    mf = midi.translate.music21ObjectToMidiFile(ritmo)
    mf.open(archivo, 'wb')
    mf.write()
    mf.close()


print('Ritmo listo')
# Generar y guardar el ritmo de batería
generar_ritmo_bateria()
