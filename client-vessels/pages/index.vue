<template>

  <v-container class="pt-10">
    <h1 class="pt-10 pb-10">Vessels</h1>

    <v-row>
      <v-col>
        <VesselsTable :loading="tableLoading" :vessels="vessels"></VesselsTable>
      </v-col>
      <v-col>1</v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts" setup>
import { type DjangoResponse } from '~/types/DjangoResponse';
import type Vessel from '~/types/Vessel';


const tableLoading = ref(false);

const vessels = ref([] as Vessel[]);

const getVessels = async () => {
  try {
    tableLoading.value = true
    const response: DjangoResponse = await $fetch('http://localhost:8000/api/vessels')
    vessels.value = response.results;
  } catch (error) {
    console.log(error)
  } finally {
    tableLoading.value = false;
  }
};

onMounted(async () => {
  await getVessels()
})
</script>