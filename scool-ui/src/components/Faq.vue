<template>
  <div class="container mt-5 e-c-wrapp past-events">
    <div class="row">
      <div class="faq" id="question1">
        <p class="question">У меня нет опыта. Подойдет ли мне данный курс</p>
        <button v-if="!question1" class="faq-open-button" @click="openFaqBlock('question1', question1)">
          <img src="../assets/images/faq-open.svg">
        </button>
        <button v-else class="faq-open-button" @click="openFaqBlock('question1', question1)">
          <img src="../assets/images/faq-close.svg">
        </button>
        <p v-if="question1">Наша система обучения построена таким образом,что наши студенты смогут беспрепятственно
          получить необходимые компетенции с «0». В нашу философию входит максимум практических занятий,через которые
          наши студенты прокачают свои скиллы на максимум возможностей. В профессию сможет погрузиться каждый студент,
          от вас  потребуется желание, усердие и дисциплина, остальное -наша задача!</p>
      </div>
      <div class="faq" id="question2">
        <p class="question">Нужно ли знать математику?</p>
        <button v-if="!question2" class="faq-open-button" @click="openFaqBlock('question2', question2)">
          <img src="../assets/images/faq-open.svg">
        </button>
        <button v-else class="faq-open-button" @click="openFaqBlock('question2', question2)">
          <img src="../assets/images/faq-close.svg">
        </button>
        <p v-if="question2">На этапе зарождения профессии– это было правдой. Но в мире все эволюционирует, в том числе
          и языки программирования. Языки стали высокотехнологичными, сложные математические функции и расчеты сегодня
          уже заложены в командах современных языков программирования. Например, один из самых популярных языков JAVA,
          айтишники называют «женским» языком. Потому самое главное качество программиста на JAVA – это память.</p>
      </div>
      <div class="faq" id="question3">
        <p class="question">.Сколько часов в неделю мне нужно уделять курсу?</p>
        <button v-if="!question3" class="faq-open-button" @click="openFaqBlock('question3', question3)">
          <img src="../assets/images/faq-open.svg">
        </button>
        <button v-else class="faq-open-button" @click="openFaqBlock('question3', question3)">
          <img src="../assets/images/faq-close.svg">
        </button>
        <p v-if="question3">Помимо регламентированного времени,отведенного под занятия в Академии, вы должны уделить
          3-4 часа в неделю на выполнение домашних заданий и 3-4 часа в неделю на индивидуальное развитие
          (чтение специализированной литературы,просмотр видео материала,участие в конференциях)</p>
      </div>
      <div class="faq" id="question4">
        <p class="question">Кто будет помогать мне на курсе?</p>
        <button v-if="!question4" class="faq-open-button" @click="openFaqBlock('question4', question4)">
          <img src="../assets/images/faq-open.svg">
        </button>
        <button v-else class="faq-open-button" @click="openFaqBlock('question4', question4)">
          <img src="../assets/images/faq-close.svg">
        </button>
        <p v-if="question4">Во время Вашего обучения вы на 100% взаимодействуете с преподавателем, также у каждой
          группы будет педагог -куратор и менеджер учебного процесса, с которым происходит взаимодействие по
          административным вопросам вашего обучения.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Faq",

  data() {
    return {
      course: {},
      question1: false,
      question2: false,
      question3: false,
      question4: false,
    }
  },

  methods: {
    openFaqBlock(blockId, question) {
      switch (blockId) {
        case 'question1': {
          this.question1 = !this.question1;
          break;
        }
        case 'question2': {
          this.question2 = !this.question2;
          break;
        }
        case 'question3': {
          this.question3 = !this.question3;
          break;
        }
        case 'question4': {
          this.question4 = !this.question4;
          break;
        }
      }
      let block = document.getElementById(blockId);
      if (question) {
        block.classList.remove('faq_active');
      } else {
        block.classList.add('faq_active');
      }
    },
  }
}
</script>

<style scoped>
.faq {
  background-color: #FFFFFF;
  border-radius: 6px;
  padding: 10px;
  margin: 10px;
  border: 0.5px solid;
  border-image: linear-gradient(to right, #eb934f, #63a9da) 47% 0;
  border-image-slice: 1;
}

.faq_active {
  box-shadow: 42px -37px 20px -31px rgb(39 170 237 / 35%),
  55px 56px 20px -47px rgb(39 170 225 / 35%),
  -41px 40px 20px -34px rgb(247 148 29 / 40%),
  -57px -54px 20px -50px rgb(247 148 29 / 40%);
  transition: box-shadow 0.8s ease;
}

.faq-open-button {
  height: 20px;
  border: none;
  float: right;
  align-items: center;
}

.faq .question {
  margin: 0;
  display: inline;
  font-weight: 500;
  font-size: 18px;
  align-items: center;
  line-height: 46px;
  border: none;
  box-shadow: 18px 14px 20px -13px rgb(39 170 237 / 35%),
  26px -18px 20px -21px rgb(39 170 225 / 35%),
  -18px 7px 20px -12px rgb(247 148 29 / 40%),
  -28px -22px 20px -22px rgb(247 148 29 / 40%);
  transition: box-shadow 0.8s ease;
}
</style>