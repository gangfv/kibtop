import jwtDecode from "jwt-decode";
import { instance } from "./Instance"
import { Cookies } from "./tools/CookieController";
import FormDataCreator from "./tools/FormDataCreator";

export const AuthApi = {
    async auth() {
        const { refresh } = Cookies.getCookies();
        return await instance.post('auth/jwt/refresh/',
            {
                "refresh": refresh || 'refresh'
            }).then(res => {
                const access = res.data.access

                const {user_id} = jwtDecode(access)
                Cookies.setCookie('access', access)

                return {userId: user_id}
            }, () => null).catch(err => console.log(err))
    },

    async registration(email, password1, password2, name, city, file) {
        const formData = !!file ? FormDataCreator({
            "phone": '',
            "first_name": '',
            "last_name": '',
            "username": email.split('@')[0]+((+new Date()).toString(16)),
            "email": email,
            "password": password1,
            "re_password": password2,
            "middle_name": name,
            "addres": city || '',
            "upload_user": file || ''
        }) : {
            "phone": '',
            "first_name": '',
            "last_name": '',
            "username": email.split('@')[0]+((+new Date()).toString(16)),
            "email": email,
            "password": password1,
            "re_password": password2,
            "middle_name": name,
            "addres": city || '',
            "upload_user": undefined
        }


        return await instance.post('auth/users/', formData)
            .then((res) => {
                return res.data
            })
    },

    async login(email, password) {

        const body = {
            "username": email,
            "password": password
        }
        
        return await instance.post('auth/jwt/create/', body)
            .then(({data}) => {

                console.log(data);

                const {access, refresh} = data

                Cookies.setCookie('access', access)
                Cookies.setCookie('refresh', refresh)

                return data
            })
    }
}

