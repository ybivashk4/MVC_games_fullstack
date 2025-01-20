
<script setup>
import Header from "@/components/Header.vue"
import Footer from "@/components/Footer.vue";

const some_bool = true;

</script>


<template>
  <Header></Header>
  <h3>Корзина</h3>
  <div class="main_bin" v-if="some_bool">
    <div class="in_bin">
      <div class="bin_card">
        <img src="/src/assets/default.png" alt="" height="122px" width="220px">
        <div>Some name</div>
        <div class="flex-column price">
          <div>
            1649 Р
          </div>
          <div style="margin-left: 100%" class="change_text_color">
            Удалить
          </div>
        </div>
      </div>
      <div class="bin_card">
        <img src="/src/assets/default.png" alt="" height="122px" width="220px">
        <div>Some name</div>
        <div class="flex-column price">
          <div>
            1649 Р
          </div>
          <div style="margin-left: 100%" class="change_text_color">
            Удалить
          </div>
        </div>
      </div>
      <div class="bin_card">
        <img src="/src/assets/default.png" alt="" height="122px" width="220px">
        <div>Some name</div>
        <div class="flex-column price">
          <div>
            1649 Р
          </div>
          <div style="margin-left: 100%" class="change_text_color">
            Удалить
          </div>
        </div>
      </div>
    </div>

    <div class="main_pay">
      <div class="to_pay">
        <div>Итого</div>
        <div>4948 Р</div>
      </div>
      <button class="auth_button" style="width: 100%">Оплатить</button>
    </div>
  </div>

  <div style="height: 40%;margin-top: 10%;margin-left: 5%" v-else>
    <div>
      <img src="/src/assets/empty_bin.svg" alt="">
    </div>
    <div>
      Ваша корзина пуста
    </div>
  </div>

  <Footer></Footer>
</template>

<script>
export default {
  name: "BinView"
}
</script>

<style scoped>
.main_bin {
  width: 80%;
  height: 80%;
  display: flex;
  flex-direction: row;
  margin-left: 10%;
  margin-top: 5%;
}

.in_bin {
  width: 60%;
  height: 90%;
  display: flex;
  flex-direction: column;
  margin-right: 5%;
}
.bin_card {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-evenly;
  flex-direction: row;
  font-weight: 500;
  font-size: 20px;
  line-height: 30px;
  background-color: #0F0F0F;
  border-radius: 10px;
  padding: 2% 0 2% 0;
}

.price {
  justify-content: space-between;
  text-align: left;
}
.main_pay {
  display: flex;
  width: 20%;
  flex-direction: column;
  align-items: center;
  font-size: 27px;
  font-weight: 700;
  line-height: 43px;
}
.to_pay {
  display: flex;
  width: 100%;
  justify-content: space-between;
  margin-bottom: 5%;
}

</style>
