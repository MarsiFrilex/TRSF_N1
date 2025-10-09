import APIClient from '@/api/client.js';


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

export const getStatuses = async () => {
    let response = await APIClient.get("/statuses");
    return response.data;
}

export const getUsers = async () => {
    const response = await APIClient.get("/accounts");
    return response.data;
}

export const getRoles = async (role_id) => {
    let response = await APIClient.get("/roles");
    return response.data;
}

export const uploadImage = async (file) => {
    let formData = new FormData();
    formData.append("file", file);

    let response = await APIClient.post("/cloud", formData, {
        headers: {
            "Content-Type": "multipart/form-data",
        },
    });
    return response.data;
}

export const registerDefect = async (title, description, fileUrl, tagId, objectId) => {
    console.log(title, description, tagId, objectId);
    let response = await APIClient.post("/defects", {
        title: title,
        description: description,
        object_id: objectId,
        tag_id: tagId,
        photo_url: fileUrl,
        registrator_id: 1,  // id текущего пользователя
        engineer_id: 1,
        status_id: 1,
        deadline: "",
    });
    return response.data;
}

export const updateDefect = async (id, status_id, deadline, engineer) => {
    let response = await APIClient.patch(`/defects/${id}`, {
        title: "",
        description: "",
        status_id: status_id,
        tag: "",
        deadline: deadline,
        registrator: "",
        engineer_id: engineer,
        photo_url: "",
    });
    return response.data;
}

export const getCurrentUser = async () => {
    let response = await APIClient.get(`/auth/me`);
    return response?.data;
}

export const loginUser = async (credentials) => {
    let response = await APIClient.post(`/auth/login`, credentials);
    return response.data;
}

export const registerUser = async (username, email, password, role_id) => {
    let response = await APIClient.post(`/accounts`, {
        email: email,
        user_name: username,
        password: password,
        role_id: role_id || 1
    });
    return response.data;
}

export const refreshToken = async (token) => {
    let response = await APIClient.post(`/auth/refresh`, {
        token
    });
    return response.data;
}

export const downloadExcel = async (id) => {
    let response = await APIClient.get(`/reports/${id}`, {
        responseType: "blob",
    });
    return response.data;
}