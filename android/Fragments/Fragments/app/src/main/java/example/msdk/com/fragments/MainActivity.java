package example.msdk.com.fragments;


import android.app.Fragment;
import android.app.FragmentManager;
import android.app.FragmentTransaction;
import android.support.v4.app.FragmentActivity;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import android.widget.Toast;


public class MainActivity extends FragmentActivity {

    private int stackLevel = 1;
    private String levelKey = "level";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if (savedInstanceState == null) {
            FragmentManager fragmentManager = getFragmentManager();
            FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();
            Fragment fm = MyFragment.newInstance(stackLevel);
            fragmentTransaction.add(R.id.fragment, fm);
            fragmentTransaction.commit();
        } else {
            stackLevel = savedInstanceState.getInt(levelKey);
        }

    }


    public void addFragment(View view) {
        stackLevel++;
        FragmentManager fragmentManager = getFragmentManager();
        FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();
        Fragment fm = MyFragment.newInstance(stackLevel);
        fragmentTransaction.setCustomAnimations(R.animator.fragment_slide_left_enter,
                R.animator.fragment_slide_left_exit,
                R.animator.fragment_slide_right_enter,
                R.animator.fragment_slide_right_exit);
        fragmentTransaction.replace(R.id.fragment, fm);
        fragmentTransaction.addToBackStack(null);
        fragmentTransaction.commit();
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
        super.onSaveInstanceState(outState);
        outState.putInt(levelKey, stackLevel);
    }

    public void popStack(View view) {
        stackLevel = stackLevel - 1 < 1 ? 1 : stackLevel - 1;
        getFragmentManager().popBackStack();
    }

    public static class MyFragment extends Fragment {

        private int count;

        static MyFragment newInstance(int count) {
            MyFragment f = new MyFragment();
            Bundle b = new Bundle();
            b.putInt("count", count);
            f.setArguments(b);
            return f;
        }

        @Override
        public void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            count = getArguments() == null ? 1 : getArguments().getInt("count");
        }

        @Override
        public View onCreateView(LayoutInflater inflater,
                                 ViewGroup container,
                                 Bundle savedInstanceState) {
            /**
             * Inflate the layout for this fragment
             */

            View v = inflater.inflate(R.layout.fragment, container, false);
            TextView tv = (TextView) v.findViewById(R.id.fragmentTextView);
            v.findViewById(R.id.fragmentTextView).setBackgroundResource(android.R.drawable.gallery_thumb);
            tv.setText("Fragment #" + count);
            return v;
        }

    }
}
