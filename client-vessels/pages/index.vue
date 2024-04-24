<template>
  <v-container class="pt-10">
    <h1 class="pt-10 pb-10">Vessels</h1>

    <v-row>
      <v-col cols="12" md="6">
        <v-text-field
          class="pb-5"
          v-model="search"
          density="compact"
          label="Search by vessel id"
          prepend-inner-icon="mdi-magnify"
          variant="solo-filled"
          flat
          hide-details
          single-line
          @input="debouncedInput"
        ></v-text-field>

        <VesselsTable :loading="tableLoading" :vessels="vessels"></VesselsTable>
        <div class="text-center">
          <v-pagination
            v-model="page"
            :length="pages"
            :total-visible="7"
          ></v-pagination>
        </div>
      </v-col>
      <v-col cols="12" md="6">
        <VesselForm />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts" setup>
import { type DjangoResponse } from '~/types/DjangoResponse';
import { debounce } from 'lodash';


import type Vessel from '~/types/Vessel';

const route = useRoute()
const router = useRouter()

const search = ref('')
const page = ref(0)
const tableLoading = ref(false);
const totalVessels = ref(0);
const vessels = ref([] as Vessel[]);

const pages = computed(() => {
  return Math.ceil(totalVessels.value / 10)
})


function queryPush(page: number) {
  const query = {
    page: page,
  }

  const queryWithSearch = {
    page: page,
    vessel: search.value
  }

  router.push({
    path: '/',
    query: search.value !== '' ? queryWithSearch : query
  })
}


const debouncedInput = debounce(async (e: any) => {
  search.value = e.target.value;

  await getVessels(1)

  queryPush(page.value);

}, 1000);

const getVessels = async (pageNumber: number = 1) => {
  try {
    tableLoading.value = true
    let url = `http://localhost:8000/api/vessels/?page=${pageNumber}`
    if (search.value !== '') {
      url = `http://localhost:8000/api/vessels/?page=${pageNumber}&vessel_id=${search.value}`
    }
    const response: DjangoResponse = await $fetch(url);
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

  if (route.query.vessel) {
    search.value = route.query.vessel.toString();
  }

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

  queryPush(page);
})
</script>