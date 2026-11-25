(function () {
  var STORAGE_KEY = "eps-lang";
  var SUPPORTED = ["ka", "en", "ru"];

  var T = {
    ka: {
      "brand.name": "EPS ქარხანა",
      "brand.factory": "ქარხანა",
      "nav.products": "პროდუქცია",
      "nav.blog": "ბლოგი",
      "nav.contact": "კონტაქტი",
      "nav.menu": "მენიუ",
      "nav.main": "მთავარი მენიუ",
      "footer.contact": "კონტაქტი",
      "footer.products": "პროდუქცია",
      "footer.site": "საიტი",
      "footer.home": "მთავარი",
      "footer.catalog": "კატალოგი",
      "footer.copy": "EPS დეკორატიული ფასადის ელემენტები, საქართველო.",
      "crumbs.home": "მთავარი",
      "crumbs.aria": "ბილიკი",
      "cta.price": "ფასის მოთხოვნა",
      "cta.request": "მოითხოვეთ ფასი",
      "cta.catalog": "კატალოგის ნახვა",
      "home.kicker": "საქართველო · EPS წარმოება",
      "home.h1": "EPS დეკორატიული ელემენტები ფასადისთვის",
      "home.lead": "კარნიზები, სვეტები, პანელები, ჩარჩოები და კრონშტეინები EPS-ისგან. წარმოება საქართველოშია, მიწოდება მთელ ქვეყანაში.",
      "home.meta.cats": "კატეგორია",
      "home.meta.products": "პროდუქტი",
      "home.meta.material": "მასალა",
      "home.cat.eyebrow": "კატალოგი",
      "home.cat.h2": "პროდუქციის კატეგორიები",
      "home.cat.lead": "აირჩიეთ კატეგორია, შემდეგ პროდუქტი – მის გვერდზე ნახავთ ხელმისაწვდომ ზომებს.",
      "home.gal.eyebrow": "პორტფოლიო",
      "home.gal.h2": "ფასადის მაგალითები",
      "home.why.eyebrow": "უპირატესობები",
      "home.why.h2": "რატომ EPS",
      "home.why.1.t": "მსუბუქია",
      "home.why.1.p": "ელემენტები ფასადს დიდ დატვირთვას არ უმატებს და მათი აწევა და დამაგრება მარტივია.",
      "home.why.2.t": "სწრაფი მონტაჟი",
      "home.why.2.p": "დამაგრება ხდება წებოვანი ხსნარით, საჭიროებისამებრ დუბელებით.",
      "home.why.3.t": "ბევრი ფორმა",
      "home.why.3.p": "პროფილები, სვეტები, კუთხის ქვები, კრონშტეინები და ორნამენტული ელემენტები.",
      "home.why.4.t": "ადგილობრივი წარმოება",
      "home.why.4.p": "ზომებისა და ვადების დაზუსტება შეგიძლიათ პირდაპირ მწარმოებელთან.",
      "home.order.eyebrow": "შეკვეთა",
      "home.order.h2": "როგორ შევუკვეთოთ",
      "home.order.1": "გამოგვიგზავნეთ ფასადის ფოტო, ნახაზი ან სასურველი მოდელების სია.",
      "home.order.2": "დავაზუსტებთ ზომებს, რაოდენობასა და ვადას.",
      "home.order.3": "გაგიგზავნით ფასს.",
      "home.order.4": "დადასტურების შემდეგ ვამზადებთ და გიგზავნით შეკვეთას.",
      "home.blog.eyebrow": "პუბლიკაციები",
      "home.blog.h2": "ბლოგი",
      "home.blog.all": "ყველა სტატია →",
      "home.blog.read": "წაკითხვა →",
      "home.blog.meta": "სტატია",
      "home.faq.eyebrow": "კითხვები",
      "home.faq.h2": "ხშირად დასმული კითხვები",
      "home.cta.eyebrow": "კონტაქტი",
      "home.cta.h2": "ფასის მოთხოვნა",
      "home.cta.lead": "გამოგვიგზავნეთ ფასადის ფოტო, ნახაზი ან მოდელების სია და დაგიზუსტებთ ფასს, ზომებსა და ვადას.",
      "products.count": "პროდუქტი",
      "products.eyebrow": "კატალოგი",
      "products.h1": "EPS ფასადის დეკორის კატალოგი",
      "products.lead": "12 კატეგორია: კარნიზებიდან სვეტებამდე და ფასადის პანელებამდე. თითოეული პროდუქტის გვერდზე ნახავთ ზომებს.",
      "contact.eyebrow": "დაგვიკავშირდით",
      "contact.h1": "კონტაქტი",
      "contact.lead": "გამოგვიგზავნეთ ფასადის ფოტო, ნახაზი ან მოდელების სია და დაგიზუსტებთ ფასს, ზომებსა და ვადას.",
      "contact.phone": "ტელეფონი",
      "contact.email": "ელფოსტა",
      "contact.address": "მისამართი",
      "contact.hours": "სამუშაო საათები",
      "contact.whatsapp": "WhatsApp",
      "contact.write": "მოგვწერეთ",
      "blog.eyebrow": "პუბლიკაციები",
      "blog.h1": "ბლოგი: EPS ფასადის დეკორი",
      "blog.lead": "რჩევები ფასადის დეკორის არჩევის, გამოყენებისა და მონტაჟის შესახებ.",
      "prod.eyebrow": "პროდუქტი",
      "prod.sizes": "ზომები",
      "prod.model": "მოდელი",
      "prod.size": "ზომა",
      "prod.related": "მსგავსი პროდუქტები",
      "prod.desc": "აღწერა და გამოყენება",
      "cat.eyebrow": "კატეგორია",
      "cat.others": "სხვა კატეგორიები",
      "cat.khis-panelebi": "ხის პანელები",
      "cat.inqeqciuri-panelebi": "ფაქტურიანი ფასადის პანელები (4 სმ)",
      "cat.kutxis-qvebi": "კუთხის ქვები",
      "cat.fanjris-charchoebi": "ფანჯრის ჩარჩოები",
      "cat.sartulis-karnizebi": "სართულის კარნიზები",
      "cat.ornamentuli-sartulis-karnizebi": "ორნამენტული სართულის კარნიზები",
      "cat.fanjris-qveda-charchoebi": "ფანჯრის ქვედა ჩარჩოები",
      "cat.ornamentuli-gvirgvinebi": "ორნამენტული გვირგვინები",
      "cat.parapetebi": "პარაპეტები და ქუდები",
      "cat.svetebi": "სვეტები",
      "cat.kronshteinebi": "კრონშტეინები",
      "cat.chiris-filebi": "ჭერის ფილები",
      "lang.label": "ენა"
    },
    en: {
      "brand.name": "EPS Factory",
      "brand.factory": "Factory",
      "nav.products": "Products",
      "nav.blog": "Blog",
      "nav.contact": "Contact",
      "nav.menu": "Menu",
      "nav.main": "Main menu",
      "footer.contact": "Contact",
      "footer.products": "Products",
      "footer.site": "Site",
      "footer.home": "Home",
      "footer.catalog": "Catalog",
      "footer.copy": "EPS decorative facade elements, Georgia.",
      "crumbs.home": "Home",
      "crumbs.aria": "Breadcrumb",
      "cta.price": "Request a quote",
      "cta.request": "Request a quote",
      "cta.catalog": "View catalog",
      "home.kicker": "Georgia · EPS manufacturing",
      "home.h1": "EPS decorative elements for facades",
      "home.lead": "Cornices, columns, panels, frames and brackets from EPS. Made in Georgia, delivered nationwide.",
      "home.meta.cats": "Categories",
      "home.meta.products": "Products",
      "home.meta.material": "Material",
      "home.cat.eyebrow": "Catalog",
      "home.cat.h2": "Product categories",
      "home.cat.lead": "Choose a category, then a product — each product page lists available sizes.",
      "home.gal.eyebrow": "Portfolio",
      "home.gal.h2": "Facade examples",
      "home.why.eyebrow": "Benefits",
      "home.why.h2": "Why EPS",
      "home.why.1.t": "Lightweight",
      "home.why.1.p": "Elements add little load to the facade and are easy to lift and install.",
      "home.why.2.t": "Fast installation",
      "home.why.2.p": "Fixed with adhesive mortar and, when needed, mechanical anchors.",
      "home.why.3.t": "Many shapes",
      "home.why.3.p": "Profiles, columns, quoins, brackets and ornamental elements.",
      "home.why.4.t": "Local production",
      "home.why.4.p": "Confirm sizes and lead times directly with the manufacturer.",
      "home.order.eyebrow": "Ordering",
      "home.order.h2": "How to order",
      "home.order.1": "Send us a facade photo, drawing or list of preferred models.",
      "home.order.2": "We confirm sizes, quantities and lead time.",
      "home.order.3": "We send you a quote.",
      "home.order.4": "After confirmation we manufacture and deliver the order.",
      "home.blog.eyebrow": "Articles",
      "home.blog.h2": "Blog",
      "home.blog.all": "All articles →",
      "home.blog.read": "Read →",
      "home.blog.meta": "Article",
      "home.faq.eyebrow": "FAQ",
      "home.faq.h2": "Frequently asked questions",
      "home.cta.eyebrow": "Contact",
      "home.cta.h2": "Request a quote",
      "home.cta.lead": "Send us a facade photo, drawing or model list and we will confirm price, sizes and timing.",
      "products.count": "products",
      "products.eyebrow": "Catalog",
      "products.h1": "EPS facade decor catalog",
      "products.lead": "12 categories: from cornices to columns and facade panels. Each product page lists sizes.",
      "contact.eyebrow": "Get in touch",
      "contact.h1": "Contact",
      "contact.lead": "Send us a facade photo, drawing or model list and we will confirm price, sizes and timing.",
      "contact.phone": "Phone",
      "contact.email": "Email",
      "contact.address": "Address",
      "contact.hours": "Working hours",
      "contact.whatsapp": "WhatsApp",
      "contact.write": "Message us",
      "blog.eyebrow": "Articles",
      "blog.h1": "Blog: EPS facade decor",
      "blog.lead": "Tips on choosing, using and installing EPS facade decoration.",
      "prod.eyebrow": "Product",
      "prod.sizes": "Sizes",
      "prod.model": "Model",
      "prod.size": "Size",
      "prod.related": "Related products",
      "prod.desc": "Description & use",
      "cat.eyebrow": "Category",
      "cat.others": "Other categories",
      "cat.khis-panelebi": "Wood panels",
      "cat.inqeqciuri-panelebi": "4 cm textured facade panels",
      "cat.kutxis-qvebi": "Corner stones",
      "cat.fanjris-charchoebi": "Window frames",
      "cat.sartulis-karnizebi": "Floor cornices",
      "cat.ornamentuli-sartulis-karnizebi": "Ornamental floor cornices",
      "cat.fanjris-qveda-charchoebi": "Window sill frames",
      "cat.ornamentuli-gvirgvinebi": "Ornamental crowns",
      "cat.parapetebi": "Parapets & caps",
      "cat.svetebi": "Columns",
      "cat.kronshteinebi": "Brackets",
      "cat.chiris-filebi": "Ceiling tiles",
      "lang.label": "Language",
      "hours.value": "Monday – Saturday, 09:00 – 18:00",
      "street.value": "19 Akhalgazrdobis Avenue",
      "city.value": "Kutaisi, 4600"
    },
    ru: {
      "brand.name": "Завод EPS",
      "brand.factory": "Завод",
      "nav.products": "Продукция",
      "nav.blog": "Блог",
      "nav.contact": "Контакты",
      "nav.menu": "Меню",
      "nav.main": "Главное меню",
      "footer.contact": "Контакты",
      "footer.products": "Продукция",
      "footer.site": "Сайт",
      "footer.home": "Главная",
      "footer.catalog": "Каталог",
      "footer.copy": "Декоративные фасадные элементы из EPS, Грузия.",
      "crumbs.home": "Главная",
      "crumbs.aria": "Навигация",
      "cta.price": "Запросить цену",
      "cta.request": "Запросить цену",
      "cta.catalog": "Смотреть каталог",
      "home.kicker": "Грузия · Производство EPS",
      "home.h1": "Декоративные элементы EPS для фасада",
      "home.lead": "Карнизы, колонны, панели, обрамления и кронштейны из EPS. Производство в Грузии, доставка по всей стране.",
      "home.meta.cats": "Категории",
      "home.meta.products": "Продукты",
      "home.meta.material": "Материал",
      "home.cat.eyebrow": "Каталог",
      "home.cat.h2": "Категории продукции",
      "home.cat.lead": "Выберите категорию, затем продукт — на странице продукта указаны доступные размеры.",
      "home.gal.eyebrow": "Портфолио",
      "home.gal.h2": "Примеры фасадов",
      "home.why.eyebrow": "Преимущества",
      "home.why.h2": "Почему EPS",
      "home.why.1.t": "Лёгкий",
      "home.why.1.p": "Элементы почти не нагружают фасад и их легко монтировать.",
      "home.why.2.t": "Быстрый монтаж",
      "home.why.2.p": "Крепление клеящим раствором и при необходимости дюбелями.",
      "home.why.3.t": "Много форм",
      "home.why.3.p": "Профили, колонны, угловые камни, кронштейны и орнаментальные элементы.",
      "home.why.4.t": "Местное производство",
      "home.why.4.p": "Размеры и сроки можно уточнить напрямую у производителя.",
      "home.order.eyebrow": "Заказ",
      "home.order.h2": "Как заказать",
      "home.order.1": "Пришлите фото фасада, чертёж или список нужных моделей.",
      "home.order.2": "Уточним размеры, количество и сроки.",
      "home.order.3": "Отправим цену.",
      "home.order.4": "После подтверждения изготовим и отправим заказ.",
      "home.blog.eyebrow": "Публикации",
      "home.blog.h2": "Блог",
      "home.blog.all": "Все статьи →",
      "home.blog.read": "Читать →",
      "home.blog.meta": "Статья",
      "home.faq.eyebrow": "Вопросы",
      "home.faq.h2": "Частые вопросы",
      "home.cta.eyebrow": "Контакты",
      "home.cta.h2": "Запросить цену",
      "home.cta.lead": "Пришлите фото фасада, чертёж или список моделей — уточним цену, размеры и сроки.",
      "products.count": "продуктов",
      "products.eyebrow": "Каталог",
      "products.h1": "Каталог фасадного декора EPS",
      "products.lead": "12 категорий: от карнизов до колонн и фасадных панелей. На каждой странице продукта — размеры.",
      "contact.eyebrow": "Свяжитесь с нами",
      "contact.h1": "Контакты",
      "contact.lead": "Пришлите фото фасада, чертёж или список моделей — уточним цену, размеры и сроки.",
      "contact.phone": "Телефон",
      "contact.email": "Эл. почта",
      "contact.address": "Адрес",
      "contact.hours": "Часы работы",
      "contact.whatsapp": "WhatsApp",
      "contact.write": "Написать",
      "blog.eyebrow": "Публикации",
      "blog.h1": "Блог: фасадный декор EPS",
      "blog.lead": "Советы по выбору, применению и монтажу фасадного декора EPS.",
      "prod.eyebrow": "Продукт",
      "prod.sizes": "Размеры",
      "prod.model": "Модель",
      "prod.size": "Размер",
      "prod.related": "Похожие продукты",
      "prod.desc": "Описание и применение",
      "cat.eyebrow": "Категория",
      "cat.others": "Другие категории",
      "cat.khis-panelebi": "Деревянные панели",
      "cat.inqeqciuri-panelebi": "Фактурные фасадные панели 4 см",
      "cat.kutxis-qvebi": "Угловые камни",
      "cat.fanjris-charchoebi": "Оконные обрамления",
      "cat.sartulis-karnizebi": "Карнизы между этажами",
      "cat.ornamentuli-sartulis-karnizebi": "Орнаментальные карнизы между этажами",
      "cat.fanjris-qveda-charchoebi": "Нижние оконные обрамления",
      "cat.ornamentuli-gvirgvinebi": "Орнаментальные короны",
      "cat.parapetebi": "Парапеты и крышки",
      "cat.svetebi": "Колонны",
      "cat.kronshteinebi": "Кронштейны",
      "cat.chiris-filebi": "Потолочная плитка",
      "lang.label": "Язык",
      "hours.value": "Понедельник – суббота, 09:00 – 18:00",
      "street.value": "пр. Ахалгазрдобы, N19",
      "city.value": "Кутаиси, 4600"
    }
  };

  var FAQ = {
    ka: [
      ["რა არის EPS ფასადის დეკორი?", "ეს არის გაფართოებული პოლისტირონისგან (EPS) დამზადებული მსუბუქი დეკორატიული ელემენტები შენობის ფასადისთვის: კარნიზები, სვეტები, ფანჯრის ჩარჩოები, კუთხის ქვები და პანელები."],
      ["რით განსხვავდება EPS დეკორი ბეტონის ან თაბაშირის დეკორისგან?", "EPS ელემენტები გაცილებით მსუბუქია, ამიტომ ფასადზე დამატებით დატვირთვას ნაკლებად ქმნის, მისი მონტაჟი კი უფრო სწრაფია."],
      ["როგორ მაგრდება EPS დეკორი ფასადზე?", "ელემენტები ფასადზე მაგრდება სპეციალური წებოვანი ხსნარით, საჭიროების შემთხვევაში დუბელებით. შემდეგ ზედაპირი იფარება დამცავი ფენით და იღებება."],
      ["შესაძლებელია თუ არა სხვა ზომის ან ფორმის ელემენტის შეკვეთა?", "დაგვიკავშირდით და გამოგვიგზავნეთ ესკიზი ან ზომები. გეტყვით, რა შეიძლება დამზადდეს."],
      ["როგორ გავიგო ფასი?", "ფასი დამოკიდებულია პროფილზე, ზომასა და რაოდენობაზე. გამოგვიგზავნეთ ფასადის ფოტო ან ნახაზი და გამოგიანგარიშებთ."]
    ],
    en: [
      ["What is EPS facade decor?", "Lightweight decorative facade elements made from expanded polystyrene (EPS): cornices, columns, window surrounds, quoins and panels."],
      ["How does EPS decor differ from concrete or plaster?", "EPS elements are much lighter, so they add less load to the facade and install faster."],
      ["How is EPS decor fixed to the facade?", "Elements are fixed with adhesive mortar and, if needed, anchors. Then the surface is coated with a protective layer and painted."],
      ["Can I order a custom size or shape?", "Contact us with a sketch or dimensions. We will tell you what can be made."],
      ["How do I get a price?", "Price depends on profile, size and quantity. Send a facade photo or drawing and we will calculate a quote."]
    ],
    ru: [
      ["Что такое фасадный декор EPS?", "Лёгкие декоративные элементы для фасада из вспененного полистирола (EPS): карнизы, колонны, обрамления окон, угловые камни и панели."],
      ["Чем EPS отличается от бетона или гипса?", "Элементы EPS намного легче, меньше нагружают фасад и монтируются быстрее."],
      ["Как крепится декор EPS на фасад?", "Крепление специальным клеящим раствором и при необходимости дюбелями. Затем поверхность покрывается защитным слоем и окрашивается."],
      ["Можно ли заказать другой размер или форму?", "Свяжитесь с нами и пришлите эскиз или размеры. Скажем, что можно изготовить."],
      ["Как узнать цену?", "Цена зависит от профиля, размера и количества. Пришлите фото или чертёж фасада — рассчитаем."]
    ]
  };

  function detect() {
    try {
      var saved = localStorage.getItem(STORAGE_KEY);
      if (SUPPORTED.indexOf(saved) !== -1) return saved;
    } catch (e) {}
    var nav = (navigator.language || "ka").toLowerCase();
    if (nav.indexOf("ru") === 0) return "ru";
    if (nav.indexOf("en") === 0) return "en";
    return "ka";
  }

  function t(lang, key) {
    return (T[lang] && T[lang][key]) || (T.ka && T.ka[key]) || key;
  }

  function apply(lang) {
    if (SUPPORTED.indexOf(lang) === -1) lang = "ka";
    document.documentElement.lang = lang === "ka" ? "ka" : lang;
    document.documentElement.setAttribute("data-lang", lang);

    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var key = el.getAttribute("data-i18n");
      var val = t(lang, key);
      if (el.getAttribute("data-i18n-attr")) {
        el.setAttribute(el.getAttribute("data-i18n-attr"), val);
      } else {
        el.textContent = val;
      }
    });

    document.querySelectorAll("[data-i18n-html]").forEach(function (el) {
      el.innerHTML = t(lang, el.getAttribute("data-i18n-html"));
    });

    // FAQ translation
    var faqItems = document.querySelectorAll(".faq-list details");
    var faq = FAQ[lang] || FAQ.ka;
    faqItems.forEach(function (d, i) {
      if (!faq[i]) return;
      var s = d.querySelector("summary");
      var p = d.querySelector("p");
      if (s) s.textContent = faq[i][0];
      if (p) p.textContent = faq[i][1];
    });

    // Localized address / hours when present
    document.querySelectorAll("[data-i18n-hours]").forEach(function (el) {
      el.textContent = lang === "ka" ? el.getAttribute("data-ka") || el.textContent : t(lang, "hours.value");
    });
    document.querySelectorAll("[data-i18n-street]").forEach(function (el) {
      if (lang === "ka") {
        el.textContent = el.getAttribute("data-ka") || el.textContent;
      } else {
        el.textContent = t(lang, "street.value") + ", " + t(lang, "city.value");
      }
    });

    document.querySelectorAll(".lang-switch [data-lang]").forEach(function (btn) {
      var on = btn.getAttribute("data-lang") === lang;
      btn.classList.toggle("is-active", on);
      btn.setAttribute("aria-pressed", on ? "true" : "false");
    });

    try {
      localStorage.setItem(STORAGE_KEY, lang);
    } catch (e) {}
  }

  function init() {
    var lang = detect();
    apply(lang);
    document.querySelectorAll(".lang-switch [data-lang]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        apply(btn.getAttribute("data-lang"));
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  window.EPS_I18N = { apply: apply, t: t, detect: detect };
})();
