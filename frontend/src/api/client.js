import axios from "axios";
import { refreshToken } from "@/api/index.js";
import { useRouter } from "vue-router"

const router = useRouter();

const APIClient = axios.create({
    baseURL: "http://localhost:8000/",
    headers: {
        "Content-Type": "application/json",
        "accept": "application/json",
    }
});

APIClient.interceptors.request.use(
    (config) => {
       let accessToken = localStorage.getItem("accessToken");
        if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`
        }
        return config;
    },
    (error) => Promise.reject(error)
)

APIClient.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;
        if ((error.response.status === 401 || error.response.status === 403) && !originalRequest._retry) {
            originalRequest._retry = true
            if (!!localStorage.getItem("accessToken") && error.response.status === 401) {
                localStorage.removeItem("accessToken");
            }
            if (error.response.status === 403 && !!localStorage.getItem("accessToken")) {
                return Promise.reject(error);
            }
            try
            {
                let tokens = await refreshToken(localStorage.getItem("refreshToken"));
                localStorage.setItem("accessToken", tokens.access_token);
                localStorage.setItem("refreshToken", tokens.refresh_token);
                originalRequest.headers.Authorization = `Bearer ${tokens.access_token}`;
                return APIClient(originalRequest);
            }
            catch (refreshError)
            {
                localStorage.removeItem("accessToken");
                localStorage.removeItem("refreshToken");
                await router.push("/login");
                return Promise.reject(refreshError)
            }
        }
        return Promise.reject(error)
    }
);

export default APIClient;