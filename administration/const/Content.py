import enum


class Content(enum.Enum):
    SUBMISSION = 'Korisnik/ca <a href="/profil/{}/">{}</a> predao/la vam je rad kojemu \
možete pristupiti na sljedećoj poveznici <a href="/prikaz/{}/">{}</a> <br> <br> '

    STUDENT_TO_MENTOR_SUBMISSION = 'Uspješno ste predali svoj rad mentoru. Status rada možete pratiti ovdje \
 <a href="/prikaz/{}/">{}</a>'
    STUDENT_TO_PRESIDENT_SUBMISSION = 'Uspješno ste predali svoj rad predjedniku povjerenstva. Status rada možete pratiti ovdje \
 <a href="/prikaz/{}/">{}</a>'

    MENTOR_VERIFICATION = 'Uspješno ste izvršili provjeru izvornosti za rad: <a href="/prikaz/{}/">{}</a>. \
Generirani obrazac o provjeri izvornosti možete preuzeti <a href="/media/{}">ovdje</a>'
    STUDENT_VERIFICATION = 'Mentor/ica je izvršio/la provjeru izvornosti za vaš rad: <a href="/prikaz/{}/">{}</a>. \
Generirani obrazac o provjeri izvornosti možete preuzeti <a href="/media/{}">ovdje</a>'

    STATUS_CHANGER = 'Uspješno ste promijenili status rada u <b>{}</b> za rad: <a href="/prikaz/{}/">{}</a>.'
    STATUS_CHANGED = 'Status vašeg rada: <a href="/prikaz/{}/">{}</a> promijenjen je u <b>{}</b>. <br> <br>'

    MENTOR_GRADE = 'Uspješno ste unijeli konačnu ocjenu za rad: <a href="/prikaz/{}/">{}</a> \
<br> <br> Ocjena: <b>{}</b> <br> Status rada: <b>{}</b>'
    STUDENT_BACHELOR_GRADE = 'Mentor/ica je unio/jela konačnu ocjenu za vaš rad: <a href="/prikaz/{}/">{}</a> \
<br> <br>Konačna ocjena: <b>{}</b> <br> Status rada: <b>{}</b>'

    ADDED_TO_COMITEE ='Dodani ste kao član povjerenstva za diplomski rad: <a href="/prikaz/{}/">{}</a>. <br> \
Nakon obrane rada na ovoj <a class="modal-trigger" data-target="grade" href="#grade" data-tg_id="{}" >poveznici</a> možete \
unesti ocjenu rada i obrane.'
    ADDED_COMITEE = 'Uspješno ste dodali članove povjerenstva za diplomski rad: <a href="/prikaz/{}/">{}</a>'
    STUDENT_ADDED_COMITEE = 'Dodani su članovi povjerenstva za vaš diplomski rad: <a href="/prikaz/{}/">{}</a> <br> <br> \
Članovi: <br>'

    COMITEE_MEMBER_ADDED_GRADE ='Uspješno ste unijeli ocjenu rada i ocjenu obrane za rad: <a href="/prikaz/{}/">{}</a><br> <br> \
Ocjena rada: <b>{}</b> <br> Ocjena obrane: <b>{}</b>'
    STUDENT_MASTER_GRADE ='Članovi povjerenstva unijeli su ocjene za vaš rad :<a href="/prikaz/{}/">{}</a> \
<br> <br>Konačna ocjena: <b>{}</b> <br> Status rada: <b>{}</b> <br> <br> Ocjene članova: <br>'

    STUDENT_CHANGED_DOCUMENT = 'Uspješno ste promijenili datoteku rada za <a href="/prikaz/{}/">{}</a>'
    PRESIDENT_CHANGED_DOCUMENT = 'Izvršena je promjena datoteke za rad <a href="/prikaz/{}/">{}</a> u ispravljenu verziju'
