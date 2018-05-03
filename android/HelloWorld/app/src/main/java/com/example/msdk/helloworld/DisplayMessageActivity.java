package com.example.msdk.helloworld;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v4.app.Fragment;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.RelativeLayout;
import android.widget.TextView;

public class DisplayMessageActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display_message);

        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

//        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
//        fab.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
//                        .setAction("Action", null)
//                        .show();
//            }
//        });
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        Intent intent = getIntent();
        String studentName = intent.getStringExtra(MainActivity.STUDENT_NAME);
        String studentGrade = intent.getStringExtra(MainActivity.STUDENT_GRADE);
        TextView name = new TextView(this);
        name.setGravity(Gravity.CENTER_HORIZONTAL);
        name.setTextSize(40);
        RelativeLayout.LayoutParams lp = new RelativeLayout.LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        lp.addRule(RelativeLayout.CENTER_HORIZONTAL, RelativeLayout.TRUE);
        lp.addRule(RelativeLayout.CENTER_VERTICAL, RelativeLayout.TRUE);
        name.setId(View.generateViewId());
        name.setText("Name: " + studentName);

        TextView grade = new TextView(this);
        grade.setGravity(Gravity.CENTER_HORIZONTAL);
        grade.setTextSize(40);
        RelativeLayout.LayoutParams grade_lp = new RelativeLayout.LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        grade_lp.addRule(RelativeLayout.CENTER_HORIZONTAL, RelativeLayout.TRUE);
        grade_lp.addRule(RelativeLayout.BELOW, name.getId());
        grade.setText("Grade: " + studentGrade);

        RelativeLayout layout = (RelativeLayout) findViewById(R.id.content);
        layout.addView(name, lp);
        layout.addView(grade, grade_lp);
    }

}
