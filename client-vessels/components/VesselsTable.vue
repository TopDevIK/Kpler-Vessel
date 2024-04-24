<template>
  <v-card>
    <v-table :loading="props.loading">
      <thead>
        <tr>
          <th class="text-left text-green">
            Vessel Id
          </th>
          <th class="text-left text-green">
            Position Time
          </th>
          <th class="text-left text-green">
            Latitude
          </th>
          <th class="text-left text-green">
            Longitude
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in vessels"
          :key="item.id"
        >                
          <td>{{ item.vessel_id }}</td>
          <td>
            {{ $dayjs(item.position_time).format('YYYY/MM/DD HH:mm:ss') }}
          </td>
          <td>
            <v-chip color="primary"> {{ item.latitude }}</v-chip>
          </td>
          <td>
            <v-chip color="primary"> {{ item.longitude }}</v-chip>
          </td>
        </tr>
      </tbody>
      
    </v-table>
  </v-card>
</template>

<script lang="ts" setup>
import type Vessel from '~/types/Vessel';

const props = defineProps({
  vessels: {
    type: Array as PropType<Vessel[]>
  },
  loading: {
    required: false,
    default: false
  }
})
</script>