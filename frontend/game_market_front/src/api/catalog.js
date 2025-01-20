import {$authHost} from "@/api/index.js";

export const getCatalog = async () => {
    const catalog = await $authHost.get('catalog')
    return catalog.data
}
