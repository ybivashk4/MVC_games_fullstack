<script setup>
import Header from "@/components/Header.vue"
import Footer from "@/components/Footer.vue";


</script>

<template>
  <Header></Header>

  <div class="main_description">
    <h3>some name</h3>
    <div class="description">
      <div class="card">
        <img
          src="/src/assets/default.png"
          alt=""
          width="350px"
          height="400px"
          style="border-radius: 20px"
        />
        <div class="under_img" >
          <div>1649 Р</div>
          <button class="auth_button">В корзину</button>
        </div>
        <button class="auth_button" style="margin-top: 5%;width: 100%">В список желаемого</button>
      </div>
      <div class="flex-column" style="margin-top: 5%">
        <div class="change_text_color up_text_description">
          <div>4.9</div>
          <div>Одиночная</div>
          <div>Открытый мир</div>
        </div>
        <div style="display: flex;margin-top: 4vh">
          <div style="text-align: left">

            <div class="change_text_color">
              Жанр
            </div>
            <div class="change_text_color">
              Язык
            </div>
            <div class="change_text_color">
              Дата выхода
            </div>
            <div class="change_text_color">
              Разработчик
            </div>
            <div class="change_text_color">
              Особенности
            </div>

          </div>

          <div style="text-align: left;margin-left: 5vh">

            <div>
              Экшен
            </div>
            <div>
              Русский
            </div>
            <div>
              30 марта 2022
            </div>
            <div>
              ybivashka productions
            </div>
            <div>
              Особенная игра
            </div>

          </div>

        </div>
        <div class="big_description">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui distinctio est culpa nam nihil atque quas officiis
        mollitia voluptas, doloremque error consectetur labore optio fugit dicta! Earum et suscipit repellat!                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui distinctio est culpa nam nihil atque quas officiis
        mollitia voluptas, doloremque error consectetur labore optio fugit dicta! Earum et suscipit repellat!                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui distinctio est culpa nam nihil atque quas officiis
        mollitia voluptas, doloremque error consectetur labore optio fugit dicta! Earum et suscipit repellat!                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui distinctio est culpa nam nihil atque quas officiis
        mollitia voluptas, doloremque error consectetur labore optio fugit dicta! Earum et suscipit repellat!                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui distinctio est culpa nam nihil atque quas officiis
        mollitia voluptas, doloremque error consectetur labore optio fugit dicta! Earum et suscipit repellat!                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui distinctio est culpa nam nihil atque quas officiis
        mollitia voluptas, doloremque error consectetur labore optio fugit dicta! Earum et suscipit repellat!                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui distinctio est culpa nam nihil atque quas officiis
        mollitia voluptas, doloremque error consectetur labore optio fugit dicta! Earum et suscipit repellat!                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui distinctio est culpa nam nihil atque quas officiis
        mollitia voluptas, doloremque error consectetur labore optio fugit dicta! Earum et suscipit repellat!                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Qui distinctio est culpa nam nihil atque quas officiis
        mollitia voluptas, doloremque error consectetur labore optio fugit dicta! Earum et suscipit repellat!
        </div>
      </div>

    </div>


  </div>


  <Footer></Footer>


</template>

<style scoped>
.card {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  width: 350px;
  margin: 5%;
}

.under_img {
  display: flex;
  justify-content: space-evenly;

  text-align: center;
  font-size: 24px;
  font-weight: 700;
  line-height: 36px;
  margin-top: 5%;
}

.main_description {
  display: flex;
  width: 80%;
  flex-direction: column;
}

.description {
  display: flex;
  flex-direction: row;
  width: 100%;
  justify-content: space-around;
  font-size: 18px;
  line-height: 27px;
  font-weight: 500;
}





.up_text_description {
  display: flex;
  justify-content: space-between;
  width: 28vh;
}


.big_description {
  text-align: left;
  width: 70%;
  margin-top: 5%;
}
</style>
