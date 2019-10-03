package com.ammar.restapitry;

import android.telecom.Call;

import retrofit2.http.Body;
import retrofit2.http.POST;

public interface UserClient {

    @POST("train")
    retrofit2.Call<Day> sendDay(@Body Day day);

}
