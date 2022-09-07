let langResourcesArr = {
  en: {
    Home: "Home",
    Shop: "Shop",
    Blog: "Blog",
    Contact: "Contact",
    About: "About",
    English: "English",
    Persion: "Persion",
    Pashto: "Pashto",
    Lang: "English",
    login: "Login",
    myaccount: "My Account",
    call: "Call Free",
    location: "Location",
    cart: "Cart",
    subtotal: "Sub Total",
    paymethod: "Payment Method",
    shipdetail: "Shipping Details",
    pay: "Pay",
    address: "Address",
    phone: "Phone",
    email: "Email",
    info: "Information",
    title1: "Gemstone Arrivals",
    title2: "Exclusive Offer  this week",
    shopping: "Shopping Now",
    bestsell: "Best Selling Products",
    ban1: "Sale Off 20% All Gamestone",
    ban1: "New Trending Collection",
    ban1: "We Believe That Good Design is Always in Season",
    newproducts: "New Products",
    popularproduct: "Popular Products",
    topnews: "Top News",

    uname: "Username or Email",
    password: "Password",
    lost: "Lost your password?",
    remember: "Remember me",

  },
  fr: {
    Home: "صفحه نخست",
    Shop: "محصولات",
    Blog: "مقالات",
    Contact: "تماس با ما ",
    About: "در باره ما",
    English: "انگلیسی",
    Persion: "دری",
    Pashto: "پشتو",
    Lang: "دری",
    login: "ورود",
    myaccount: "حساب من",
    call: "شماره تماس",
    location: "موقیعت",
    cart: "سبد خرید",
    subtotal: "مجموع",
    paymethod: "نوعیت پرداخت",
    shipdetail: "جزیات ارسال",
    pay: "پرداخت",
    address: "آدرس",
    phone: "شماره تماس",
    email: "ایمیل",
    info: "معلومات عمومی",
    title1: " جدید ترین سنگ های قیمتی",
    title2: "تخفیف های این هفته",
    shopping: "خرید نمایید",
    bestsell: "پر فروش ترین محصولات",
    ban1: "و ۲۰ فیصد تخفیف برای همه محصولات",
    ban2: "جدیدترین مجموعه ها",
    ban3: "ما باور داریم بهترین دیزان ها همیشه پوشیدنیست",
    newproducts: "جدیدترین محصولات",
    popularproduct: "مشهورترین محصولات",
    topnews: "اخبار جدید",
    
    uname: "اسم کاربری و یا ایمیل",
    password: "رمز عبور",
    lost: "آیا رمز عبور را فراموشش کردید؟?",
    remember: "به یاد داشته باشید",

  },
  pa: {
    Home: " لمری صفحه",
    Shop: "محصولات",
    Blog: "مقالونه",
    Contact: "تماس",
    About: "زموژ په اره",
    English: "انگلیسی",
    Persion: "دری",
    Pashto: "پښتو",
    Lang: "پښتو",
    login: "ورود",
    myaccount: "زموژ حساب",
    call: "تماس شمیره",
    location: "موقیعت",
    cart: " د خرید سبد",
    subtotal: "مجموع",
    paymethod: "نوعیت پرداخت",
    shipdetail: "جزیات ارسال",
    pay: "پرداخت",
    address: "آدرس",
    phone: " اریکی شمیره",
    email: "ایمیل",
    info: "معلومات عمومی",
    title1: " جدید ترین سنگ های قیمتی",
    title2: "تخفیف های این هفته",
    shopping: "خرید نمایید",
    bestsell: "پر فروش ترین محصولات",
    ban1: "و ۲۰ فیصد تخفیف برای همه محصولات",
    ban1: "جدیدترین مجموعه ها",
    ban1: "ما باور داریم بهترین دیزان ها همیشه پوشیدنیست",
    newproducts: "جدیدترین محصولات",
    popularproduct: "مشهورترین محصولات",
    topnews: "اخبار جدید",
    test: "تست",

    uname: " د کاربر نوم او یا ایمیل",
    password: " د عبور رمز ",
    lost: "آیا رمز عبور را فراموشش کردید؟?",
    remember: "به یاد داشته باشید",

  },
};

function changeLanguage(clickedLangChoiceId) {
    localStorage.setItem('language', clickedLangChoiceId);
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
  $(".greet").each(function(){
          let currentlyIteratedGreetKey = $(this).attr("key"); 
          let localizedValForGreetKey =
          langResourcesArr[clickedLangChoiceId][currentlyIteratedGreetKey]; 
          $(this).text(localizedValForGreetKey); 
  });
}

var language = localStorage.getItem('language');
if(!language){
  language = "en";
}
changeLanguage(language);
