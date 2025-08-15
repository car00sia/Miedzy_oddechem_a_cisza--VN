define r = Character("Rob")
define c = Character("Charon", what_prefix="«", what_suffix="»")

label start:
    scene black
    play sound "wypadeksamochodowy.mp3"
    pause 1

    scene styx with fade
    show charon at center
    r "Gdzie... ja... jestem?"
    c "Między oddechem a ciszą."
    r "Słucham?"
    c "Nie pamiętasz?... Wymuszenie pierwszeństwa, wolny czas reakcji, huk, dźwięk tłuczonego szkła?" 
    c "Nienajlepszy z ciebie kierowca" 
    r "Miałem wypadek... Jak dobrze, że żyję."
    c "Muszę cię zmartwić – nie żyjesz."
    r "Co?... Czy ja jestem w niebie?"
    c "Czemu wy wierzycie w te bajeczki? Jesteś nad Styks"
    r "Styks? Jak w mitach??"
    c "Zostawię to bez komentarza..."
    c "Pozwól, że się przedstawię, Charon - przewoźnik zmarłych dusz"
    r "Rob"
    c "Większość dusz płynie na pole Asfodelowe. Wieczne błądzenie w szarości..."
    r "A co ze mną?"
    c "Sędziowie jeszcze nie wydali wyroku. Możesz od razu odpłynąć z nimi… albo spróbować naprawić to, co obciąża twoją duszę"
    r "Jak to zrobić"
    c "Gdy wypłyniemy na Styks, po drodze napotkamy wiry wodne. Każdy z nich przeniesie cię do momentu w twoim życiu, w którym popełniłeś błąd. Masz jedną szansę na każdy z nich."
    r "A jeśli mi się nie uda?"
    c "Tartarus... - Uwierz mi, nawet nie chcę tam przepływać. Ja nie mam żołądka, a i tak robi mi się niedobrze na samą myśl."
    r "..."
    c "Więc jak, Rob? Naprawiasz błędy i walczysz o Elizjum i wieczne szczęście? Czy wolisz od razu spłynąć na Pola i zniknąć w szarej nicości?"

    menu:
        "Decyduję się zawalczyć o swoją wieczność, ryzykując wylądowaniem w najniższej części krainy podziemia":
            r "Dobra, spróbujmy. Co mam do stracenia?"
	"Nie ryzykuję, decyduję się na wieczne błądzenie w szarości":
            r "Nie... To zbyt duże ryzyko."
        
            

    return
