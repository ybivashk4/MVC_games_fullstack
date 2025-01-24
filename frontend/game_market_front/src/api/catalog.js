import {$authHost} from "@/api/index.js";

export const getCatalog = async () => {
    const catalog = await $authHost.get('catalog')
    return catalog.data
}

export const getGame = async (id) => {
    const game = await $authHost.get('catalog/' + id)
    return game.data
}
