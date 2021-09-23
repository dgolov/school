<template>
  <div id="lesson-list">
    <div v-for="lesson in lessonList" :key="lesson.id" class="accordion-item">
      <h2 class="accordion-header" id="flush-heading1">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                data-bs-target="#flush-collapse1" aria-expanded="false"
                aria-controls="flush-collapse1">{{ lesson.theme }}
        </button>
      </h2>
      <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne"
           data-bs-parent="#accordionFlushExample">
        <div class="accordion-body">
          <p>{{ lesson.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Lessons",
  props: {
    course: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      lessonList: {}
    }
  },
  created() {
    this.loadLessonList();
  },
  methods: {
    async loadLessonList() {
      this.lessonList = await fetch(
          `${this.$store.getters.getServerUrl}/courses/${this.course.id}/lessons`
      ).then(response => response.json());
    }
  }
}
</script>

<style scoped>

</style>