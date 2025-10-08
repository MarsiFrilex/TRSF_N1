import axios from "axios";

const APIClient = axios.create({
    baseURL: "http://localhost:8000/",
    headers: {
        "Content-Type": "application/json",
        "accept": "application/json",
    }
});

export const getAllObjects = async () => {
    let response = await APIClient.get("/objects");
    return response.data;
}

export const addNewObject = async (address, description) => {
    let response = await APIClient.post("/objects", {address, description});
    return response.data;
}

export const getDefectsByObjectId = async (id) => {
    let response = await APIClient.get(`/defects?object_id_filter=${id}`);
    return response.data;
}

export const getTags = async () => {
    let response = await APIClient.get("/tags");
    return response.data;
}

export const uploadImage = async (file) => {

}

export const registerDefect = async (title, description, fileUrl, tagId, objectId) => {
    let response = await APIClient.post("/defects", {
        title: title,
        description: description,
        object_id: objectId,
        tag_id: tagId,
        registrator_id: 1,  // id текущего пользователя
        engineer_id: 1,
        status_id: 1,
        deadline: 1,
    });
    return response.data;
}

