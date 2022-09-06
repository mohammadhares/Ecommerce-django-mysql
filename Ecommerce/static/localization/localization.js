let langResourcesArr = {
  en: {
    Home: "Home",
    Shop: "Shop",
    Blog: "Blog",
    Contact: "Contact",
    About: "About",
  },
  fr: {
    Home: "صفحه نخست",
    Shop: "محصولات",
    Blog: "مقالات",
    Contact: "تماس با ما ",
    About: "در باره ما",
  },
  pa: {
    Home: " لمری صفحه",
    Shop: "محصولات",
    Blog: "مقالونه",
    Contact: "تماس",
    About: "زموژ په اره",
  },
};

function changeLanguage(clickedLangChoiceId) {

    if(clickedLangChoiceId !== "en"){
        let lists = document.querySelectorAll('.direct');
        for(let i = 0; i < lists.length; i++){
            lists[i].classList.add('rtl');
        }
    }else{
        let lists = document.querySelectorAll('.direct');
        for(let i = 0; i < lists.length; i++){
            lists[i].classList.remove('rtl');
        }
    }
  $(function () {
    $("#greetings-list li")
      .children(".greet")
      .each(function () {
        let currentlyIteratedGreetKey = $(this).attr("key"); 
        let localizedValForGreetKey =
          langResourcesArr[clickedLangChoiceId][currentlyIteratedGreetKey]; 
        $(this).text(localizedValForGreetKey); 
      });
  });
}
