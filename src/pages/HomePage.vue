<template>
  <div>
    <Banner
      :class="showBanner ? 'hidden' : ''"
      v-bind:closeCallback="closeBanner"
    />
    <div class="relative bg-white overflow-hidden h-screen flex items-center">
      <div class="max-w-7xl mx-auto mr-12">
        <main class="ml-4 lg:ml-0">
          <div class="">
            <h1
              class="
                font font-extrabold
                tracking-tight
                text-gray-900 text-6xl
                mb-12
              "
            >
              Get the job done<span class="text-primary">.</span>
            </h1>
            <h3
              class="
                text-xl
                font font-bold
                tracking-tight
                text-gray-900
                sm:text-4xl
                mb-0
              "
            >
              Students
            </h3>
            <p class="mt-4 text-lg text-gray-500 mb-4">
              Launch the next step in you career.
            </p>
            <h3
              class="
                text-xl
                font font-bold
                tracking-tight
                text-gray-900
                sm:text-4xl
                mb-0
              "
            >
              Employers
            </h3>
            <p class="mt-4 text-lg text-gray-500">
              Hire the next generation of talent.
            </p>
            <div class="mt-10">
              <a
                href="/browse"
                class="
                  inline-block
                  text-center
                  bg-primary
                  border border-transparent
                  rounded-md
                  py-3
                  px-8
                  font-medium
                  text-white
                  hover:bg-primaryOffset
                  mr-4
                  mb-2
                  lg:mb-0
                "
                >Find Jobs</a
              >
            </div>
          </div>
        </main>
      </div>
      <div class="mx-auto ml-0">
        <img src="../img/jobhunt.svg" class="max-h-80" />
      </div>
    </div>
  </div>
</template>

<script>
import Banner from "../components/Banner.vue";
import { ref } from "vue";
export default {
  name: "HomePage",
  components: {
    Banner,
  },
  setup() {
    const showBanner = ref(false);
    function closeBanner() {
      showBanner.value = true;
    }
    return {
      showBanner,
      closeBanner,
    };
  },
};
</script>
