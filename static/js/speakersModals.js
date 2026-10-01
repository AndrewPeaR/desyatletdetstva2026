let myPopup1;
let myPopup2;
let myPopup3;
let myPopup4;

document.addEventListener("DOMContentLoaded", () => {
  myPopup1 = new Popup({
    id: "my-popup1",
    title: "Беляев Максим Анатольевич",
    content: `
            {subtitle-font}[г. Уфа]
            <img src='static/img/speakers/speaker1.jpg' alt="speaker one" style="border-radius: 8px;">
            {bold}[● Руководитель Городской службы медиации г. Уфы (на базе МБОУ ДО ЦППМСП «Развитие» г. Уфы), главный семейный медиатор Республики Башкортоста]
            {bold}[● Руководитель центра примирительных технологий и общественного взаимодействия федерального государственного бюджетного образовательного учреждения высшего образования «Башкирский государственный педагогический университет им. М. Акмуллы»]
            {bold}[● Член экспертного совета по развитию служб медиации и примирения в образовательных организациях при Министерстве Просвещения Российской Федерации]
            {bold}[● Член Координационного совета по Государственной семейной политике при Правительстве Республики Башкортостан]
            {bold}[● Руководитель рабочей группы по развитию медиации при Координационном совете по Государственной семейной политике при Правительстве Республики Башкортостан]
            {bold}[● Член Совета (президиума) Башкортостанского отделения Ассоциации юристов России]
            {bold}[● Член общественного экспертного совета при Уполномоченном по правам детей Республики Башкортостан]
            {bold}[● Автор книг, учебников, статей по медиации и другим примирительным процедурам]
            {bold}[● Автор федерального курса «Семейная медиация» на базе «Академии Знание» от Российского общества «Знание»]
        `,
    widthMultiplier: 1.8,
    titleSizeMultiplier: 0.6,
    titleColor: "rgb(47, 80, 31)",
    titleMargin: "0",
    backgroundColor: "#fff",
    css: `
        .popup-body p{
            margin-top: 1%;
            margin-bottom: 1%;
            text-align: left;
        }
    `,
  });
  myPopup2 = new Popup({
    id: "my-popup2",
    title: "Силенок Инна Казимировна",
    content: `
            {subtitle-font}[г. Краснодар]
            <img src='static/img/speakers/speaker2.jpg' alt="speaker ецщ" style="border-radius: 8px;">
            {bold}[● Психолог, психотерапевт, травмотерапевт, кризисный психолог Народного Фронта, бизнес-тренер]
            {bold}[● Психотерапевт Единых Реестров профессиональных психотерапевтов Европы и Мира]
            {bold}[● Вице-президент, преподаватель международного уровня и аккредитованный супервизор Общероссийской профессиональной психотерапевтической лиги]
            {bold}[● Президент Межрегиональной общественной организации «Развитие психологической помощи», руководитель Центра психологии и бизнес-консультирования «ЛОГОС»]
            {bold}[● Главный редактор Всероссийской психологической газеты «Золотая лестница» и руководитель горячей линии бесплатной психологической помощи]
            {bold}[● Автор 7 психологических книг и более 70 обучающих курсов, техник и методик, в том числе, по работе с тяжелой психологической травмой, член Союза писателей России, почетный член Ассоциации спортивных психологов]
        `,
    widthMultiplier: 1.8,
    titleSizeMultiplier: 0.6,
    titleColor: "rgb(47, 80, 31)",
    titleMargin: "0",
    backgroundColor: "#fff",
    css: `
        .popup-body p{
            margin-top: 1%;
            margin-bottom: 1%;
            text-align: left;
        }
    `,
  });
  myPopup3 = new Popup({
    id: "my-popup3",
    title: "Ковалёва Анастасия Викторовна",
    content: `
            {subtitle-font}[г. Москва]
            <img src='static/img/speakers/speaker3.jpg' alt="speaker three" style="border-radius: 8px;">
            {bold}[● Член Экспертного совета при Уполномоченном при Президенте Российской Федерации по правам ребенка]
            {bold}[● Юрист, медиатор]
            {bold}[● Кризисный психолог]
            {bold}[● Эксперт комитета Государственной Думы]
            {bold}[● Автор международных и российских проектов по работе с семьей и детьми]
        `,
    widthMultiplier: 1.8,
    titleSizeMultiplier: 0.6,
    titleColor: "rgb(47, 80, 31)",
    titleMargin: "0",
    backgroundColor: "#fff",
    css: `
        .popup-body p{
            margin-top: 1%;
            margin-bottom: 1%;
            text-align: left;
        }
    `,
  });
  myPopup4 = new Popup({
    id: "my-popup4",
    title: "Милованов Иван Петрович ",
    content: `
            {subtitle-font}[г. Санкт-Петербург]
            <img src='static/img/speakers/speaker4.jpg' alt="speaker four" style="border-radius: 8px;">
            {bold}[● Директор по инновациям Центра Системных Инициатив]
            {bold}[● Резидент экспертного клуба «Мастерской новых медиа»]
            {bold}[● Эксперт круглогодичного молодёжного образовательного центра «Профилактика и Безопасность»]
            {bold}[● Эксперт Палаты молодых законодателей Совета Федерации РФ]
            {bold}[● Выпускник «Мастерской новых медиа»]
        `,
    widthMultiplier: 1.8,
    titleSizeMultiplier: 0.6,
    titleColor: "rgb(47, 80, 31)",
    titleMargin: "0",
    backgroundColor: "#fff",
    css: `
        .popup-body p{
            margin-top: 1%;
            margin-bottom: 1%;
            text-align: left;
        }
    `,
  });
});

document.querySelector("#speaker1").addEventListener("click", () => {
  myPopup1.show();
});
document.querySelector("#speaker2").addEventListener("click", () => {
  myPopup2.show();
});
document.querySelector("#speaker3").addEventListener("click", () => {
  myPopup3.show();
});
document.querySelector("#speaker4").addEventListener("click", () => {
  myPopup4.show();
});

// await sleep(2000);
// myPopup.hide();
