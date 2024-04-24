<template>
  <v-container class="pt-10">
    <h1 class="pt-10 pb-10">Vessels</h1>

    <v-row>
      <v-col>
        <VesselsTable :loading="tableLoading" :vessels="vessels"></VesselsTable>
        <div class="text-center">
          <v-pagination
            v-model="page"
            :length="pages"
            :total-visible="7"
          ></v-pagination>
        </div>
      </v-col>
      <v-col>1</v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts" setup>
import { type DjangoResponse } from '~/types/DjangoResponse';
import type Vessel from '~/types/Vessel';

const route = useRoute()
const router = useRouter()

const page = ref(0)
const tableLoading = ref(false);
const totalVessels = ref(0);
const vessels = ref([] as Vessel[]);

const pages = computed(() => {
  return Math.ceil(totalVessels.value / 10)
})


const getVessels = async (pageNumber: number = 1) => {
  try {
    tableLoading.value = true
    const response: DjangoResponse = await $fetch(`http://localhost:8000/api/vessels/?page=${pageNumber}`)
    vessels.value = response.results;
    totalVessels.value = response.count;
    page.value = pageNumber;;
  } catch (error) {
    console.log(error)
  } finally {
    tableLoading.value = false;
  }
};

onMounted(async () => {
  if (route.query.page) {
    await getVessels(Number(route.query.page))
  } else {
    await getVessels()
  }
})

watch(page, async (page, previous) => {
  if (previous !== 0) {
    await getVessels(page)
  }

  router.push({
    path: '/',
    query: { page: page }
  })
})
</script>