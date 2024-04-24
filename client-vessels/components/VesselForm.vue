<template>
  <v-alert
    v-model="alert.show"
    :text="alert.text"
    :title="alert.title"
    :type="alert.type ? alert.type : 'success'"
    variant="tonal"
    closable
    class="mb-5"
  ></v-alert>
  <v-card class="pa-10" >
    <v-form ref="form" @submit.prevent="validateVessel" id="save-vessel-form">
      <v-text-field
        v-model="vesselId"
        :counter="10"
        :rules="[v => !!v || 'Vesseld id is required']"
        label="Vessel Id"
        required
      ></v-text-field>

      <v-text-field
        v-model="positionTime"
        type="datetime-local"
        label="Position time"
        :rules="[v => !!v || 'Position time is required']"
        required
      ></v-text-field>

      <v-text-field
        v-model="latitude"
        :rules="[v => !!v || 'Latitude id is required']"
        label="Latitude"
        required
      ></v-text-field>
  
      <v-text-field
        v-model="longitude"
        :rules="[v => !!v || 'Longitude id is required']"
        label="Longitude"
        required
      ></v-text-field>

      <v-btn
        :loading="loading"
        class="mt-4 float-right"
        color="success"
        type="submit"
        append-icon="mdi-content-save"
        form="save-vessel-form"
      >
        Save Vessel
      </v-btn>
    </v-form>
  </v-card>
</template>

<script setup>

const alert = reactive({
  show: false,
  text: 'Success',
  title: 'Vessel Saved',
  type: 'success',
})

const loading = ref(false)
const form = ref(null)
const vesselId = ref('')
const positionTime = ref('')
const latitude = ref('')
const longitude = ref('')

const saveVessel = async () => {
  try {
    loading.value = true
    const response = await $fetch('http://localhost:8000/api/vessels/', {
      method: 'post',
      body: {
        vessel_id: vesselId.value,
        position_time: positionTime.value,
        latitude: latitude.value,
        longitude: longitude.value
      }
    })
    alert.text = `Vessel ${response.vessel_id} saved`
    alert.title = 'Success'
    alert.type = 'success'
    alert.show = true

    form.value.reset()
  } catch (error) {

    let errorMsg = ''

    if (error.data.non_field_errors) {
      errorMsg += error.data.non_field_errors.join(', ')
    }

    if (error.data.latitude) {
      errorMsg += error.data.latitude.join(', ')
    }
  
    if (error.data.longitude) {
      errorMsg += error.data.longitude.join(', ')
    }

    alert.text = `${errorMsg}`
    alert.title = 'Error'
    alert.type = 'error'
    alert.show = true
  } finally {
    loading.value = false
  }
}

const validateVessel = async () => {
  const { valid } = await form?.value?.validate()
  if (valid) saveVessel() 
}


</script>