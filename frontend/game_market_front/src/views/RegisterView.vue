<script setup>
import {RouterLink, useRouter} from 'vue-router'
import {useAuthStore} from "@/stores/AuthStore.js";
import VLoader from "@/components/VLoader.vue";
import Header_non_auth from "@/components/Header_non_auth.vue";
import Footer from "@/components/Footer.vue";

const authStore = useAuthStore();
const router = useRouter()
const register = async () => {
    await authStore.register()
    if (!authStore.authError) {
        console.log('no error register')
        await authStore.login()
        await router.push('/')
    } else {
        console.log('error register', authStore.authError)
    }
}
</script>


<template>
  <Header_non_auth></Header_non_auth>
  <div>
    <div class="up_auth_text">
      <span>Регистрация</span>
    </div>
    <form class="auth" @submit.prevent="register" @keydown.enter.prevent="register">


      <small v-if="authStore.authError">
                        {{ authStore.authError.username?.toString() || authStore.authError.detail }}
      </small>


      <div class="custom_br"></div>
      <div>
        <div class="auth_text">Логин</div>
        <input type="text" v-model="authStore.username" placeholder="Введите логин"/>
      </div>

      <small v-if="authStore.authError">
        {{ authStore.authError.password?.toString() || authStore.authError.detail }}
      </small>

      <div class="custom_br"></div>
      <div class="auth_text">
        <div>Пароль</div>
        <input type="password" v-model="authStore.password" placeholder="Введите Пароль"/>
      </div>
      <div class="custom_br"></div>
      <button class="auth_button" type="submit" v-if="!authStore.loading">Создать аккаунт</button>
      <VLoader class="auth-loader" v-else></VLoader>
      <div class="custom_br"></div>
      <div style="color: #999">
        Уже есть аккаунт? <router-link to="/login" class="a">Войти</router-link>
      </div>
    </form>
  </div>
  <Footer></Footer>

</template>




<style scoped>

</style>
