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