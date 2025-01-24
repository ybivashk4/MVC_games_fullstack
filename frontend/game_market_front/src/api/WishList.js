import {$authHost} from "@/api/index.js";

// data is game from catalog
export const AddToWishList = async (game_information_id) => {
    const game = await $authHost.post('wishlist', {game_information_id})
    return game.data
}

export const AddToBin = async (game_information_id) => {
    const game = await $authHost.post('bin', {game_information_id})
    return game.data
}
export const DeleteGameFromWishlist = async (id) => {
  return await $authHost.delete(`wishlist/${id}`)
}

export const DeleteGameFromBin = async (id) => {
  return await $authHost.delete(`bin/${id}`)
}

export const GetFromWishList = async (id) => {
    const game = await $authHost.get('wishlist/'+id)
    return game.data
}

export const GetFromToBin = async (id) => {
    const game = await $authHost.get('bin/'+id)
    return game.data
}
export const getAllFromBin = async () => {
    const games = await $authHost.get('bin')
    return games.data
}
export const getAllFromWishlist = async () => {
    const games = await $authHost.get('wishlist')
    return games.data
}
export const delAllFromBin = async () => {
  return await $authHost.delete(`bin`)
}
/*

import {$authHost} from "@/api/index.js";

export const getTask = async () => {
    const tasks = await $authHost.get('tasks')
    return tasks.data
}

export const createTask = async (text) => {
    const {task} = await $authHost.post('tasks', {
        text, is_done: false
    })
    return {task}
}

export const updateTask = async ({id, text, is_done}) => {
    const {data} = await $authHost.put(`tasks/${id}`, {
        text, is_done
    })
    return {data}
}

export const deleteTask = async (id) => {
    return await $authHost.delete(`tasks/${id}`)

 */
