<script setup lang="ts">
    import { useHistoryStore } from "@/stores/history"

    const { records, getLocalDate, getLocalTime } = useHistoryStore()

</script>

<template>
    <v-table>
        <thead>
            <tr>
                <th class="text-center">Date</th>
                <th class="text-center">Contact</th>
                <th class="text-center">Message</th>
                <th class="text-center">Category_message</th>
                <th class="text-center">Time</th> 
            </tr>
        </thead>
       
        <tbody>
            <tr v-for="record in records">
                
                <td class="text-center">
                    {{ getLocalDate(record["date_time"]) }}
                </td>
                
                <td class="text-center">
                    {{ record["contact__full_name"] }}
                </td>
                
                <td class="text-center">
                    {{ record["message__content"] }}
                </td>
                
                <td class="text-center">
                    {{ record["message__category__name"] }}
                </td>
                
                <td class="text-center">
                    {{ getLocalTime(record["date_time"]) }}
                </td>
            </tr>
        </tbody> 
    
    </v-table>
</template>