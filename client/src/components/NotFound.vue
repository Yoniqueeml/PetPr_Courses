<template>
  <section>
    <b-container class="py-4">
      <b-row>
        <b-col>
          <h2>Не найдено</h2>
          <p>Мы не смогли найти то, что вам нужно :(</p>
          <router-link to="/"><button>Вернуться к ресурсам</button></router-link>
          <img
            src="@/assets/404.png"
            alt="404 - Page Not Found"
            class="img-fluid d-block mx-auto image-callout"
          />
        </b-col>
      </b-row>
    </b-container>
  </section>
</template>
