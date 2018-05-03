package com.example.msdk.helloworld;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;

public class ServicesAndBroadcast extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_services_and_broadcast);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        FloatingActionButton startService = (FloatingActionButton) findViewById(R.id.startService);
        startService.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startService();
            }
        });

        FloatingActionButton stopService = (FloatingActionButton) findViewById(R.id.stopService);
        stopService.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                stopService();
            }
        });

        FloatingActionButton startBroadcast = (FloatingActionButton) findViewById(R.id.broadcast);
        startBroadcast.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startBroadcast();
            }
        });

        getSupportActionBar().setDisplayHomeAsUpEnabled(true);
    }

    public void startService() {
        startService(new Intent(getBaseContext(), MyService.class));
    }

    public void stopService() {
        stopService(new Intent(getBaseContext(), MyService.class));
    }

    public void startBroadcast() {
        sendBroadcast(new Intent().setAction("com.example.msdk.CUSTOM_INTNET"));
    }

}
