import streamlit as st
import os
import re

def clean_text(text_string):
    text_str = str(text_string)
    pattern = r'([0-9$%\&./\-:]+)'
    fixed_html = re.sub(pattern, r'<span style="font-family:\'Inter\', sans-serif; font-weight:800; font-size:inherit;">\1</span>', text_str)
    return fixed_html

st.set_page_config(
    page_title="Performance Strength & Fitness",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        @font-face {
            font-family: 'RacingMarkPSF';
            src: url('static/racing_mark_race.otf') format('opentype');
            font-weight: normal;
            font-style: normal;
        }
        /* Core Dark Theme Setting */
        .stApp {
            background-color: #0F1011;
            color: #FFFFFF;
            font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif !important;
        }
        
        /* High-Impact Performance Typography */
        h1 {
            color: #A3FF12 !important;
            font-family: 'RacingMarkPSF', sans-serif !important;
            text-transform: uppercase;
            letter-spacing: 3px !important;
            font-size: 3.5rem !important;
            text-shadow: 3px 3px 5px rgba(0,0,0,0.9);
            margin-bottom: 0px !important;
        }
            
        h3 {
            color: #A3FF12 !important;
            font-family: 'RacingMarkPSF', sans-serif !important;
            text-transform: uppercase;
            letter-spacing: 1px !important;
            border-left: 5px solid #A3FF12;
            padding-left: 12px;
            margin-top: 30px !important;
            margin-bottom: 15px !important;
        }
            
        h4 {
            font-family: 'RacingMarkPSF', sans-serif !important;
            text-transform: uppercase;
            letter-spacing: 1px !important;
            color:#A3FF12 !important;
        }
        
        .stSelectbox, .stMultiSelect, div[data-baseweb="select"], option, label, p {
            fint-family: 'Inter', 'Helvetica Neue', Arial, sans-serif !important;
        }
        
        /* Premium Container Cards styling */
        div[data-testid="stContainer"] {
            background-color: #16181A !important;
            border: 1px solid #26292B !important;
            border-radius: 12px !important;
            padding: 24px !important;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5) !important;
        }

        /*Descriptions & List Spacing Polish */
        .stMarkdown ul, .stMarkdown li {
            font-size: 1.05rem !important;
            line-height: 1.6 !important;
            letter-spacing: 0.3px !important;
            color: #E2E8F0 !important;
        }
        .stMarkdown li {
            margin-bottom: 8px !important;
        }   
        /* Forcing Buttons to Match Your Real Logo Colorway */
        div.stButton > button, div.stLinkButton > a {
            background-color: #8EE600 !important;
            color: #000000 !important;
            font-weight: bold !important;
            font-family: 'RacingMarkPSF', sans-serif !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            border: none !important;
            border-radius: 6px !important;
            transition: transform 0.2s ease, background-color 0.2s ease !important;
        }
        
        /* Subtle interactive hover pop effect */
        div.stButton > button:hover, div.stLinkButton > a:hover {
            transform: scale(1.02) !important;
            background-color: #A3FF12 !important;
            color: #FFFFFF !important;
        }
        div.stAlert {
            background-color: #1A1C1E !important;
            border-left: 5px solid #A3FF12 !important;
            color: #FFFFFF !important
        }
        
        span.price-display, .stMarkdown h2 {
            font-family: 'RacingMarkPSF', sans-serif !important;
            letter-spacing: 1px !important;
            font-size: 2.2rem !important;
            color: #A3FF12 !important;
        }
    </style>
""", unsafe_allow_html=True)

def load_image(path, fallback_url):
    if os.path.exists(path):
        return path
    return fallback_url

LOGO_IMG = load_image("images/logo.jpg", None)
HERO_IMG = load_image("images/hero.jpg", "https://unsplash.com")
FACILITY_IMG = load_image("images/facility.jpg", "https://unsplash.com")
CLASS_IMG = load_image("images/class.jpg", "https://unsplash.com")
EXT_IMG = load_image("images/exterior.jpg", "https://unsplash.com")
OWNER_IMG = load_image("images/owner.jpg", "https://unsplash.com")

header_col1, header_col2 = st.columns([1, 6])
with header_col1:
    if LOGO_IMG:
        st.image(LOGO_IMG, width=110)
    else:
        st.title("PSF")

with header_col2:
    st.markdown("""
        <style>
            @font-face {
                font-family: 'RacingMarkPSF';
                src: url('https://jsdeliver.net') format('opentype');
                font-weight: normal;
                font-style: normal;
            }
                
            .exact-logo-header {
                font-family: 'RacingMarkPSF', Arial, sans-serif !important;
                color: #A3FF12 !important;
                font-size: 3.4rem !important;
                text-transform: uppercase !important;
                letter-spacing: 1px !important;
                margin-bottom: 0px !important;
                line-height: 1.1 !important;
                text-shadow: 3px 3px 5px rgba(0,0,0,0.9) !important;
            }
        </style>
        <h1 class="exact-logo-header">PERFORMANCE STRENGTH <span style="font-family: 'Inter', sans-serif;">&</span> FITNESS</h1>
    """, unsafe_allow_html=True)
    st.markdown("<p style='color: #8A9099; font-size: 1.1rem; margin-top 2px;'>Alexander City's Premier Training Facility</p>", unsafe_allow_html=True)

page = st.segmented_control(
    "Navigate",
    options=["🏠 Home", "🏋️ Amenities & Gear", "🤝 Meet The Owner", "❓ FAQs", "📱 GymMaster Portal"], 
    default="🏠 Home",
    label_visibility="collapsed"
)

st.markdown("<hr style='border-top: 1px solid #2D3135;'>", unsafe_allow_html=True)

if page == "🏠 Home":
    with st.container():
        st.image(HERO_IMG, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with st.container():
        st.markdown('<h2 style="font-family:\'RacingMarkPSF\', sans-serif; font-weight:bold; text-transform:uppercase; color:#A3FF12; margin-bottom:10px;">💳 MEMBERSHIP OPTIONS <span style="font-family:\'Inter\', sans-serif; font-weight:800;">&</span> RATES</h2>', unsafe_allow_html=True)
        st.markdown('<p style=font-family:\'Inter\', sans-serif; color:#FFFFFF;">Performance Strength <span style="font-weight:bold;">&</span Fitness offers flexible upfront terms and automated monthly drafts directly through GymMaster.</p>', unsafe_allow_html=True)

        price_col1, price_col2, price_col3 = st.columns(3)

        with price_col1:
            st.markdown("<h4 style+'color:#A3FF12;'>🎟️ CASUAL ENTRY</h4>", unsafe_allow_html=True)
            st.markdown('<p style="color:#A3FF12; font-family:\'RacingMarkPSF\', sans-serif; font-size:1.75rem; font-weight:bold; margin:0;"><span style="font-family:\'Inter\', sans-serif;">$7.28</span> <span style="font-size:1rem; color:#8A9899;">/ DAY PASS</span></p>', unsafe_allow_html=True)
            st.write("**💳 ONE-TIME PAYMENT**")
            st.write("• Valid for 1 single day only!\n• Paid directly on the GymMaster app\n• Access expires automatically-no recurring billing")
            st.link_button("🛒 Purchase Day Pass", "https://psfstrength.gymmasteronline.com/portal/")
        
        with price_col2:
            with st.container():
                st.markdown("<h4 style='color:#A3FF12;'>🔄️ AUTOMATED DRAFT</h4>", unsafe_allow_html=True)
                st.markdown('<p style="color:#A3FF12; font-family:\'RacingMarkPSF\', sans-serif; font-size:1.75rem; font-weight:bold; margin:0;"><span style="font-family:\'Inter\', sans-serif;">$31.20</span> <span style="font-size:1rem; color:#8A9899;">/ MONTH</span></p>', unsafe_allow_html=True)
                st.write("**⚠️ AUTOMATIC RECURRING DRAFT**")
                st.write("• Automatically billed monthly\n• Deducted on the day you originally join\n• Continued access until you request a cancellation")
                st.link_button("🛒 Purchase Draft", "https://psfstrength.gymmasteronline.com/portal/")
        
        with price_col3:
            with st.container():
                st.markdown("<h4 style='color:#A3FF12;'>🏷️ MEMBERSHIP PLANS</h4>", unsafe_allow_html=True)

                term_options = {
                    "Month-to-Month": 36.40,
                    "2-Month Plan": 72.80,
                    "3-Month Plan": 109.20,
                    "4-Month Plan": 145.60,
                    "6-Month Plan": 218.40,
                    "12-Month Plan (Best Value!)": 374.40
                }
                selected_term = st.selectbox("Choose a Plan Term:", list(term_options.keys()))
                st.markdown(f'<p style="color:#A3FF12; font-family:\'RacingMarkPSF\', sans-serif; font-size:1.75rem; font-weight:bold; margin:0;"><span style="font-family:\'Inter\', sans-serif;">${term_options[selected_term]:.2f}</span> <span style=font-size:1rem; color:#8A9899;">UPFRONT TOTAL</span></p>', unsafe_allow_html=True)
                st.write("**💳 ONE-TIME PAYMENT**")
                st.write("• Paid fully upfront via your app profile\n• Membership ends automatically at the term limit\n• Will NOT auto-renew or draft your account")
                st.link_button("🛒 Purchase Your Plan Today", "https://psfstrength.gymmasteronline.com/portal/")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("💡 **Ready to purchase?** Click any button above to manage your membership instantly via the **GymMaster Web Portal**, or download the **GymMaster Member app** on your phone to complete your profile setup!")
    
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        with st.container():
            st.markdown("### 🏋️ ELITE FACILITY EQUIPMENT")
            st.write(
                "We focus on real results through functional strength training, athletic conditioning,"
                "and expert-guided programs. Our gym features top-tier equipment optimized to help you "
                "lift heavier, move faster, and build lasting structural resilience."
            )
            st.image(FACILITY_IMG, use_container_width=True)
    
    with col2:
        with st.container():
            st.markdown("### 👥 MISSION DRIVEN COMMUNITY")
            st.write(
                "You aren't just buying another gym membership; you are joining an elite goal-driven community. "
                "Our environment is designed to eliminate plateaus, keep you motivated, and push past your physical "
                "performance boundaries safely."
            )
            st.image(CLASS_IMG, use_container_width=True)

    st.markdown("<br><hr style='border-top: 1px solid #2D3135;'>", unsafe_allow_html=True)
    foot_col1, foot_col2 = st.columns(2)
    with foot_col1:
        st.markdown("##### 📍 VISIT THE FACILITY")
        st.write("**Performance Strength & Fitness**\n625 Alex City Shopping Center\nAlexander City, AL 35010")

        st.image(EXT_IMG, use_container_width=True)
    with foot_col2:
        st.markdown("##### 🕒 CONTACT & HOURS")
        st.write("📞 **Phone:** [256-496-8043](tel:2564968043) | 📧 **Email:** [Send an Email](mailto:psfstrength@gmail.com)")
        st.write("• **Members:** 24/7 Keyless Fob Entry Enabled\n• **Staffed Hours:** Mon-Fri: 6:00 AM - 7:30 PM | Sat: 8:00 AM - 12:00 PM")

elif page == "🏋️ Amenities & Gear":
    st.markdown(f"<h3>⚡ PREMIUM AMENITIES {clean_text('&')} RECOVERY SERVICES</h3>", unsafe_allow_html=True)
    st.write(
        "Performance Strength & Fitness isn't just a place to lift, it is a place that offers an all-inclusive performance "
        "and recovery ecosystem. Explore our specialized amenities available directly to active members."
    )

    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)

    with row1_col1:
        with st.container():
            st.markdown(f"<h4 style='color:#A3FF12;'>⛳ THE {clean_text('19')}TH HOLE GOLFS SIMULATOR</h4>", unsafe_allow_html=True)
            st.write(
                "Rain or shine, keep your golf game sharp year-round. Our state-of-the-art virtual simulator "
                "allows you to analyze your swing metrics, practice drives, or play legendary 18-hole courses "
                "with crisp performance feedback data."
            )
            st.markdown(f"<p style='color:#A3FF12; font-weight:bold; maring-bottom:2px'>{clean_text('SIMULATOR HOURLY RATES:')}</p>", unsafe_allow_html=True)
            st.write(f"<p style=margin:0;'>{clean_text('*Bring Your Own Clubs:** $35.00 / Hour | *Clubs Provided by PSF:* $40.00 / Hour')}</p>", unsafe_allow_html=True)
            st.write("<span style='color:#8A9099; font-size:0.9rem;'>🎯 Book and lock in your simulator window ahead of time in your GymMaster portal</span>", unsafe_allow_html=True)
    
    with row1_col2:
        with st.container():
            st.markdown("<h4 style='color:#A3FF12;'>🧴 IN-HOUSE SUPPLEMENT SHOP</h4>", unsafe_allow_html=True)
            st.write(
                "Fuel your training sessions and maximize your muscle recovery. Our front desk features a dedicated "
                "supplement retail space carrying premium brand items, including high-quality protein powders, "
                "essential amino acids, pre-workouts, and general fitness gear. Stop by the desk to browse "
                "our current inventory options."
            )
            st.write("<span style='color:#8A9099; font-size:0.9rem;'>🛍️ Current pricing and item choices are available at the front desk!</span>", unsafe_allow_html=True)
    
    with row2_col1:
        with st.container():
            st.markdown(f"<h4 style='color:#A3FF12;'>💆 MASSAGE THERAPY ROOM</h4>", unsafe_allow_html=True)
            st.write(
                "Training breaks muscle down, but recovery is where real progress happens. Ease chronic tightness, "
                "relieve joint soreness, and optimize total-body flexibility inside our private massage therapy room "
                "designed for high-performance athletic restoration cycles."
            )
            st.markdown(f"<p style='color:#A3FF12; font-weight:bold; margin-bottom:2px;'>{clean_text('🕒 MASSAGE HOURS & RATES:')}</p>", unsafe_allow_html=True)
            st.write(f"<p style='margin:0;'>{clean_text('Availability: Every Thursday from 3:00 PM - 7:00 PM | **Rates:** 30 Minutes: $55.00 | 45 Minutes: $75.00')}</p>", unsafe_allow_html=True)
            st.write(f"<p style-'margin:0;'>{clean_text('📞 Booking: Appointment Only - Call (256) 307-0145 to secure your slot today!')}</p>", unsafe_allow_html=True)
    
    with row2_col2:
        with st.container():
            st.markdown("<h4 style='color:#A3FF12;'>☀️ PREMIUM TANNING BED</h4>", unsafe_allow_html=True)
            st.write(
                "Keep a clean, stage-ready look year-round. Our facility features professional, high-output "
                "tanning booths maintained with maximum sanitary protocols. Perfect for bodybuilders finishing down "
                "prep cycles or casual members looking for quick bronze upkeep."
            )
            st.markdown("<p style='color:#A3FF12; font-weight:bold; margin-bottom:2px;'>🔑 HOW IT WORKS:</p>", unsafe_allow_html=True)
            st.write("• **Cost:** Included with all standard gym memberships\n• **Process:** Simply walk in, lock the private room door, tan, clean up after yourself, and head back out to the training floor!")
    
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<h4 style='color:#A3FF12;'>🥋 AKT COMBATIVES ACADEMY OF CENTRAL ALABAMA</h4>", unsafe_allow_html=True)
        st.write(
            "Take your conditioning, balance, and self-defense skills to an elite level. "
            "Our open-mat martial arts division offers highly structured, realisitic combatives training "
            "built for all skill levels, physical backgrounds, and age groups."
        )

        combatives_col1, combatives_col2 = st.columns(2)
        with combatives_col1:
            st.markdown("<p style='color:#A3FF12; font-weight:bold; margin-bottom:2px;'>📅 WEEKLY CLASS SCHEDULE (Tuesdays & Thursdays):</p>", unsafe_allow_html=True)
            st.write(
                "• **Kids Classes (Ages 5-7):** 5:15 PM - 5:45 PM\n"
                "• **Kids Classes (Ages 8-12):** 5:15 PM - 6:15 PM\n"
                "• **Teens & Adults (Ages 13+):** 6:30 PM - 7:30 PM"
            )
        
        with combatives_col2:
            st.markdown("<p style='color:#A3FF12; font-weight:bold; margin-bottom:2px;'>🎟️ GET STARTED: FREE 1-WEEK ONBOARDING PASS</p>", unsafe_allow_html=True)
            st.write(
                "Experience the training environment completely risk-free. Your onboarding pass includes "
                "your first two introductory classes entirely free."
            )
            st.write("🥋 **Contact:** Reach out directly to Associate Instructor **Sensei Benjamin Bluhm** to activate your trial.")

        st.write("📞 **Phone:** Call [334-209-5024](tel:3342095024) | 📧 **Email:** [Send an Email](mailto:ben@aktcombatives.com)")

elif page == "🤝 Meet The Owner":
    with st.container():
        st.markdown("<h2 style='font-family: RacingMarkPSF; color: #FFFFFF; margin-bottom: 25px;'>MEET THE OWNER</h2>", unsafe_allow_html=True)

        col_img, col_text = st.columns([1, 1.5])

        with col_img:
            st.image(OWNER_IMG, use_container_width=True)
        
        with col_text:
            st.markdown("""
            <h3 style='color: #4dfb4d; margin-top: 0;'>OWNER: JOSH BISHOP</h3>
                        
            <p style='font-size: 1.15rem; line-height: 1.6;'>
            Born and raised in Alexander City, Josh Bishop is deeply committed to
            building the strongest and healthiest community in town. A graduate of Benjamin
            Russell High School and CACC, Josh took the reins of Performance Strength & Fitness
            in September of 2025 with one clear goal in mind: To raise the bar for local training.
            </p>
            
            <p style='font-size: 1.15rem; line-height: 1.6;'>
            As a competitive bodybuilder and owner of JCC Construction, Josh brings
            a unique blend of athletic discipline and hands-on grit to the facility. He has personally
            spearheaded the gym's massive modern renovations ranging from rare, elite machinery that
            no other local gym has, to building out his very own golfing simulator with the creation of
            "The 19th Hole" which is PSF's premier indoor golfing simulator.
            </p>
                        
            <p style='font-size: 1.15rem; line-height: 1.6;'>
            Under his signature #BYLTBYJB training, Josh believes fitness isn't just about spinning your wheels-
            it's about building personal discipline, confidence, and lifelong health through clear goals,
            meal planning, body composition tracking, and accountability. Whether you're a student-athlete, 
            a fellow lifter, or you're somebody just getting into fitness, Josh and the PSF Family are here
            to ensure you get the results you're looking for. Come by, check out everything we have to offer,
            and say hello!
            </p>
            """, unsafe_allow_html=True)

elif page == "❓ FAQs":
    st.markdown("### 💬 FREQUENTLY ASKED QUESTIONS")
    st.write("Got questions? We have clear answers to get you started smoothly.")

    with st.expander("What are your hours of operation?"):
        st.write("We provide 24/7 keyless-fob entry for our members! Staffed hours run Monday-Friday from 6:00 AM to 7:30 PM, and Saturday from 8:00 AM to 12:00 PM.")
    
    with st.expander("Can I try out the gym before committing to a membership?"):
        st.write("Yes. With our Day Pass for just $7.28, you can spend the day in our facility but the Day Pass is only good for one day only so make the most out of your visit.")
    
    with st.expander("Do you require long-term contracts, or do you offer month-to-month memberships?"):
        st.write("We offer a straightforward month-to-month plan with no cancellation hassles as well as other flexible plans that go all the way up to 12-months which can be managed, renewed, or upgraded directly through the GymMaster Member Portal.")
    
    with st.expander("How does booking work for The 19th Hole indoor golf simulator?"):
        st.write("The 19th Hole can be booked through the GymMaster Member Portal. Our current rates are listed below:")
        st.write("• $35.00 per hour (Bringing your own clubs)")
        st.write("• $40.00 per hour (Clubs provided by PSF)")
    
    with st.expander("Do I need to sign up for classes or amenities in advance?"):
        st.write("Yes. Because we limit slots to maintain absolute quality and equipment availability, everything must be set up inside your GymMaster Portal prior to arrival.")

    with st.expander("Can beginners adapt to your performance programming?"):
        st.write("Absolutely. Every single barbell, cardio, or conditioning layout can be scaled and modified by our staff to fit your starting experience level safely.")

    with st.expander("What kind of equipment do you have to offer?"):
        st.write("Unlike corporate commercial gyms, we offer rare, elite strength and bodybuilding machinery specifically sourced to maximize your training mechanics. From specialized leg presses and unique leverage pieces to plate-loaded classics, we have equipment you won't find anywhere else in the area.")


elif page == "📱 GymMaster Portal":
    import datetime
    st.markdown("### 🖥️ ONLINE MEMBER ACCOUNT HUB")
    st.write(
        "Access your complete Performance Strength & Fitness account layout from any device. "
        "Log in below to manage bookings, track workouts, view your attendance streak, or update your billing profiles natively."
    )

    btn_col1, btn_col2, btn_col3 = st.columns(3)
    with btn_col1:
        st.link_button("📅 Book Simulator / Open Gym", "https://psfstrength.gymmasteronline.com/portal/book")
    with btn_col2:
        st.link_button("📊 View My Workout Logs", "https://psfstrength.gymmasteronline.com/portal/login")
    with btn_col3:
        st.link_button("💳 Update Payment Method", "https://psfstrength.gymmasteronline/portal/login")

    st.markdown("<br>", unsafe_allow_html=True)

    if "total_visits" not in st.session_state:
        st.session_state.total_visits = 14
    if "current_streak" not in st.session_state:
        st.session_state.current_streak = 3
    if "best_streak" not in st.session_state:
        st.session_state.best_streak = 8
    if "checked_in_dates" not in st.session_state:
        today = datetime.date.today()
        st.session_state.checked_in_dates = {
            today - datetime.timedelta(days=1),
            today - datetime.timedelta(days=2),
            today - datetime.timedelta(days=5),
            today - datetime.timedelta(days=6),
            today - datetime.timedelta(days=7),
        }
    
    with st.container():
        st.markdown("<h4 style='color#A3FF12;'>📊 LIVE ATTENDANCE <span style='font-family: sans-serif; padding: 0 4px;'>&</span> STREAK TRACKER</h4>", unsafe_allow_html=True)

        if st.button("🔑 TAP TO CHECK IN TO THE GYM"):
            today_date = datetime.date.today()

            if today_date in st.session_state.checked_in_dates:
                st.warning("💪 You are already checked in for today! Get after it on the training floor!")
            else:
                st.session_state.checked_in_dates.add(today_date)
                st.session_state.total_visits += 1

                yesterday = today_date - datetime.timedelta(days=1)
                if yesterday in st.session_state.checked_in_dates:
                    st.session_state.current_streak += 1
                else:
                    st.session_state.current_streak = 1
                
                if st.session_state.current_streak > st.session_state.best_streak:
                    st.session_state.best_streak = st.session_state.current_streak
                
                st.success("🎉 Check-in verified! Your attendance and live streaks have been updated.")

        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            st.metric(label="Total Visits Logged", value=st.session_state.total_visits)
        with m_col2:
            st.metric(label="Current Attendance Streak", value=f"{st.session_state.current_streak} Days 🔥")
        with m_col3:
            st.metric(label="All-Time Best Streak", value=f"{st.session_state.best_streak} Days 👑")
    
    st.markdown("<br>", unsafe_allow_html=True)

    left_col, right_col = st.columns([2, 1])

    with left_col:
        with st.container():
            st.markdown("#### 🔒 SECURE ACCOUNT PORTAL GATEWAY")
            st.write("Desktop users can complete all profile adjustments using the secure verification window below:") 

            with st.container(border=True):
                st.markdown(
                    """
                    <div style='text-align: center; padding: 25px 10px;'>
                        <h3 style='color: #a3e635; margin: 0 0 10px 0; font-family: sans-serif;'>Performance Strength <span style="font-family: sans-serif; padding: 0 px;">&</span> Fitness</h3>
                        <p style='color: #9ca3af; font-size: 14px; margin-bottom: 20px;'>Official Member Dashboard Connection</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.link_button(
                    "🚀 Launch Member Portal",
                    "https://psfstrength.gymmasteronline.com/portal",
                    use_container_width=True
                )

                st.markdown(
                    """
                    <p style='font-size: 11px; color: #6b7280; text-align: center; margin: 15px 0 0 0;'>
                        🔒 Encrypted via GymMaster Online. Opens in a secure external window to guarantee successful session logins.
                    </p>
                    """,
                    unsafe_allow_html=True
                )
        
        st.markdown("<br>", unsafe_allow_html=True)

        with st.container():
            st.markdown("#### 📅 DIGITAL ATTENDANCE CALENDAR")
            st.write("Review all of the days you've successfully logged training outputs inside the facility:")

            selected_calendar_date = st.date_input(
                "Gym Visit Calendar Logs Viewer:",
                value=datetime.date.today(),
                label_visibility="collapsed"
            )

            if selected_calendar_date in st.session_state.checked_in_dates:
                st.markdown(f"✅ **Status:** Verified Visit on **{selected_calendar_date.strftime('%B %d, %Y')}**")
            else:
                st.markdown(f"❌ **Status:** No check-in data found for **{selected_calendar_date.strftime('%B %d, %Y')}**")

    with right_col:
        with st.container():
            st.markdown("#### 📱 PREFER THE APP?")
            st.write(
                "On the move? Everything stays perfectly synchronized in real time. "
                "Download the 'GymMaster Member' app to scan your phone at the door for 24/7 access."
            )

            st.markdown(
                "• 🍎 [Download for Apple / iOS](https://apps.apple.com/us/app/gymmaster-member/id1297093746)\n"
                "• 🤖 [Download for Android](https://play.google.com/store/apps/details?id=com.treshna.memberportal&hl=en_US)"
            )

        st.info("💡 **Login Tip:** Use the exact email address you registered with at the gym counter to unlock your portal profiles.")                   