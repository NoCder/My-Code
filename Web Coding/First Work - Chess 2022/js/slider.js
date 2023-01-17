/**
    <div class="swiper-slide">
        <div id="card">
            <img class="Image" src=" ">
            <p class="Name"> </p>
            <p class="Rate"> </p>
            <p class="Desc"> </p>
        </div>
    </div>
 */
document.addEventListener("DOMContentLoaded", function(){
    for (let i=0; i < grMasters.length; i++) {
        const list = document.getElementById('swiper');

        const swiperBase = document.createElement("div");
        const card = document.createElement("div");
        const img = document.createElement("img");
        const name = document.createElement("p");
        const rate = document.createElement("p");
        const desc = document.createElement("p");

        var obj = Object.values(grMasters[i]);

        img.className = "Image";
        img.src = obj[3];

        name.className = "Name";
        name.innerHTML = obj[0];

        rate.className = "Rate";
        rate.innerHTML = "Rate " + obj[1];

        desc.className = "Desc";
        desc.innerHTML = obj[2];

        card.id = "Card";
        card.appendChild(img);
        card.appendChild(name);
        card.appendChild(rate);
        card.appendChild(desc);

        swiperBase.className = "swiper-slide";
        swiperBase.appendChild(card);

        console.log(swiperBase);
        list.appendChild(swiperBase);
    }
});

const swiper = new Swiper('.sample-slider', {
    loop: true,
    speed: 3000,
    slidesPerView: 4,      
    autoplay: {
        delay: 0,
    },
});