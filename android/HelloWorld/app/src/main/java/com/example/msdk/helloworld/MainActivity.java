package com.example.msdk.helloworld;

import android.Manifest;
import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.content.res.Resources;
import android.net.Uri;
import android.support.design.widget.FloatingActionButton;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Gravity;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private int count = 0;
    private String msg = "Android: ";
    public final static String STUDENT_NAME = "com.example.masdk.hellowrold.STUDENT_NAME";
    public final static String STUDENT_GRADE = "com.example.masdk.hellowrold.STUDENT_GRADE";
    private final int MY_PERMISSIONS_REQUEST_CALL_PHONE = 0;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        FloatingActionButton  fab = (FloatingActionButton) findViewById(R.id.serviceActivityBtn);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
               startServiceAndBroadcastActivity();

            }


        });
    }

    private void startServiceAndBroadcastActivity() {
        Intent in = new Intent(this, ServicesAndBroadcast.class);
        startActivity(in);
    }

    public void setContentView(View view) {
        TextView text = (TextView) findViewById(R.id.msg);
        count = ++count % 2;

        if (count == 1) {
            text.setText(R.string.other_text);
            text.setBackgroundResource(R.drawable.bubbleother);
        }
        else {
            text.setText(R.string.hello_world);
            text.setBackgroundResource(R.drawable.bubblemine);
        }
    }

    public void startActivity(View view) {
        Intent intent = new Intent(this, DisplayMessageActivity.class);
        EditText studentName = (EditText) findViewById(R.id.student_name);
        EditText studentGrade = (EditText) findViewById(R.id.student_grade);
        String name = studentName.getText().toString();
        String grade = studentGrade.getText().toString();
        intent.putExtra(STUDENT_NAME, name);
        intent.putExtra(STUDENT_GRADE, grade);
        startActivity(intent);
    }


    public void call(View view) {
        if (ContextCompat.checkSelfPermission(this,
                Manifest.permission.CALL_PHONE)
                != PackageManager.PERMISSION_GRANTED) {
            // if permission denied, ask for permission.
            ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.CALL_PHONE}, MY_PERMISSIONS_REQUEST_CALL_PHONE);
        } else {
            // if permission was granted, call function,
            callIntent();
        }

    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String permissions[], int[] grantResults) {
        switch (requestCode) {
            case MY_PERMISSIONS_REQUEST_CALL_PHONE: {
                // If request is cancelled, the result arrays are empty.
                if (grantResults.length > 0
                        && grantResults[0] == PackageManager.PERMISSION_GRANTED) {

                    // permission was granted, yay! Do the
                    // contacts-related task you need to do.
                    callIntent();

                } else {

                    // permission denied, boo! Disable the
                    // functionality that depends on this permission.
                }
                return;
            }

            // other 'case' lines to check for other
            // permissions this app might request
        }
    }

    private void callIntent() {
        EditText phoneText = (EditText) findViewById(R.id.phone_number);
        String phone = "tel:" + phoneText.getText().toString();
        Intent intent = new Intent(Intent.ACTION_CALL);
        intent.setData(Uri.parse(phone));
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.CALL_PHONE) != PackageManager.PERMISSION_GRANTED) {
            // TODO: Consider calling
            //    ActivityCompat#requestPermissions
            // here to request the missing permissions, and then overriding
            //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
            //                                          int[] grantResults)
            // to handle the case where the user grants the permission. See the documentation
            // for ActivityCompat#requestPermissions for more details.
            return;
        }
        startActivity(intent);
    }

    public void startActivityLP(View view) {
        Intent in = new Intent(this, LPActivity.class);
        startActivity(in);

    }

    public void traslationActivity(View view) {
        Intent in = new Intent(this, FragmentTranslation.class);
        startActivity(in);
    }
}
