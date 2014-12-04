from pydub import AudioSegment

note1 = AudioSegment.from_ogg("A3.ogg")
note2 = AudioSegment.from_ogg("A4.ogg")
note3 = AudioSegment.from_ogg("E4.ogg")
note4 = AudioSegment.from_ogg("AS4.ogg")
note5 = AudioSegment.from_ogg("B3.ogg")
note6 = AudioSegment.from_ogg("B4.ogg")
note7 = AudioSegment.from_ogg("C4.ogg")
note8 = AudioSegment.from_ogg("C5.ogg")
note9 = AudioSegment.from_ogg("CS5.ogg")
note10 = AudioSegment.from_ogg("CS4.ogg")


bizarre_sound =  note1[:1000] + note2[:1000] + note3[:1000] + note4[:1000] + note5[:1000] + note6[:1000] + note7[:1000] + note8[:1000] + note9[:1000] + note10[:1000]

bizarre_sound.export("Test.ogg",format="ogg")
