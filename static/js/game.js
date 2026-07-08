let currentRegionId = null;
let currentLevelId = null;
let isAdmin = false;

const AVATARS = ['👤', '👨‍💻', '👩‍💻', '🧑‍💻', '🤖', '🦸', '🦸‍♀️', '🧙', '🧙‍♀️', '🐱', '🐶', '🦊', '🐼', '🐨', '🐯', '🦁', '🐸', '🦄', '👾', '🤪', '😎', '🤓', '🧐', '😺'];
let npcAvatar = '👩‍🏫';
let npcName = '富富';
let currentPlayerAvatar = null;

document.addEventListener('DOMContentLoaded', function() {
    Promise.all([
        fetch('/api/player'),
        fetch('/api/npc_config')
    ])
    .then(([playerRes, npcRes]) => Promise.all([playerRes.json(), npcRes.json()]))
    .then(([playerData, npcConfig]) => {
        isAdmin = playerData.is_admin || false;
        currentPlayerAvatar = playerData.avatar || '👤';
        npcAvatar = npcConfig.avatar || '👩‍🏫';
        npcName = npcConfig.name || '富富';
        console.log('Player loaded, isAdmin:', isAdmin);
        console.log('NPC config loaded:', npcAvatar, npcName);
        loadWorldMap();
    })
    .catch(() => {
        loadWorldMap();
    });
    
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const section = this.dataset.section;
            switchSection(section);
        });
    });
});

function showAchievementModal(achievements) {
    if (!achievements || achievements.length === 0) return;
    
    const overlay = document.createElement('div');
    overlay.className = 'achievement-modal-overlay';
    
    let currentIndex = 0;
    
    function showNextAchievement() {
        if (currentIndex >= achievements.length) {
            overlay.remove();
            return;
        }
        
        const achievement = achievements[currentIndex];
        
        overlay.innerHTML = `
            <div class="achievement-modal">
                <div class="achievement-icon">🏆</div>
                <h3 class="achievement-title">🎉 成就解锁！</h3>
                <h2 class="achievement-name">${achievement.name}</h2>
                <p class="achievement-desc">${achievement.description}</p>
                <div class="achievement-reward">
                    <i class="fas fa-coins"></i>
                    <span>+${achievement.reward} 金币</span>
                </div>
                <button class="achievement-btn" onclick="this.closest('.achievement-modal-overlay').querySelector('.achievement-modal').style.transform = 'scale(0.5)'; setTimeout(() => window.showNextAchievement(), 300);">
                    太棒了！
                </button>
            </div>
        `;
        
        document.body.appendChild(overlay);
        
        setTimeout(() => {
            overlay.classList.add('show');
        }, 50);
        
        createConfetti();
        
        currentIndex++;
    }
    
    window.showNextAchievement = showNextAchievement;
    showNextAchievement();
}

function createConfetti() {
    const colors = ['#FFC107', '#FF5722', '#E91E63', '#00FFFF', '#00FF88'];
    for (let i = 0; i < 30; i++) {
        const confetti = document.createElement('div');
        confetti.className = 'confetti';
        confetti.style.left = Math.random() * 100 + '%';
        confetti.style.background = colors[Math.floor(Math.random() * colors.length)];
        confetti.style.animationDelay = Math.random() * 2 + 's';
        confetti.style.animationDuration = (3 + Math.random() * 2) + 's';
        document.body.appendChild(confetti);
        
        setTimeout(() => confetti.remove(), 5000);
    }
}

function switchSection(sectionId) {
    document.querySelectorAll('.section').forEach(el => {
        el.classList.remove('active');
        el.classList.add('hidden');
    });
    
    const target = document.getElementById(sectionId);
    if (target) {
        target.classList.remove('hidden');
        target.classList.add('active');
    }
    
    if (sectionId === 'world-map') {
        loadWorldMap();
    } else if (sectionId === 'quests') {
        loadQuests();
    } else if (sectionId === 'shop') {
        loadShop();
    } else if (sectionId === 'achievements') {
        loadAchievements();
    } else if (sectionId === 'leaderboard') {
        loadLeaderboard();
    } else if (sectionId === 'inventory') {
        loadInventory();
    } else if (sectionId === 'admin-settings') {
        loadAdminSettings();
    }
    
    if (isAdmin) {
        document.getElementById('adminSettingsNav').style.display = 'block';
    }
}

function loadWorldMap() {
    fetch('/api/world_map')
        .then(response => response.json())
        .then(progress => {
            console.log('World map data:', progress);
            
            if (progress.length > 0 && progress[0].hasOwnProperty('is_admin')) {
                isAdmin = progress[0].is_admin;
                console.log('Admin status from backend:', isAdmin);
            }
            
            const container = document.getElementById('mapContainer');
            container.innerHTML = '';
            
            const mapTitle = document.createElement('div');
            mapTitle.className = 'map-title';
            mapTitle.textContent = 'CYBER ISLAND';
            container.appendChild(mapTitle);
            
            const cyberGrid = document.createElement('div');
            cyberGrid.className = 'cyber-grid';
            container.appendChild(cyberGrid);
            
            for (let i = 0; i < 8; i++) {
                const hex = document.createElement('div');
                hex.className = 'cyber-hex';
                hex.style.left = `${10 + (i % 4) * 25}%`;
                hex.style.top = `${15 + Math.floor(i / 4) * 40}%`;
                hex.style.animationDelay = `${i * 0.8}s`;
                container.appendChild(hex);
            }
            
            for (let i = 0; i < 15; i++) {
                const particle = document.createElement('div');
                particle.className = 'cyber-particle';
                particle.style.left = `${Math.random() * 90 + 5}%`;
                particle.style.top = `${Math.random() * 80 + 10}%`;
                particle.style.animationDelay = `${Math.random() * 10}s`;
                particle.style.animationDuration = `${8 + Math.random() * 6}s`;
                container.appendChild(particle);
            }
            
            ['tl', 'tr', 'bl', 'br'].forEach(corner => {
                const el = document.createElement('div');
                el.className = `cyber-corner ${corner}`;
                container.appendChild(el);
            });
            
            const regionIcons = {
                'day1': '🏠',
                'day2': '🌲',
                'day3': '🕳️',
                'day4': '🏰',
                'day5': '⛰️',
                'day6': '📋',
                'day7': '⭕',
                'day8': '📖',
                'day9': '🔄',
                'day10': '📚',
                'day11': '💻',
                'day12': '🌿',
                'day13': '👥',
                'day14': '🏗️',
                'day15': '🏔️',
                'day16': '✨',
                'day17': '🔑',
                'day18': '📁',
                'day19': '🔍',
                'day20': '💎'
            };
            
            const positions = [
                { x: 80, y: 100 },
                { x: 250, y: 150 },
                { x: 420, y: 100 },
                { x: 580, y: 150 },
                { x: 750, y: 100 },
                { x: 900, y: 160 },
                { x: 50, y: 280 },
                { x: 220, y: 330 },
                { x: 380, y: 270 },
                { x: 550, y: 330 },
                { x: 720, y: 270 },
                { x: 880, y: 340 },
                { x: 100, y: 460 },
                { x: 270, y: 510 },
                { x: 440, y: 450 },
                { x: 610, y: 510 },
                { x: 780, y: 450 },
                { x: 150, y: 630 },
                { x: 350, y: 680 },
                { x: 550, y: 620 }
            ];
            
            for (let i = 0; i < progress.length - 1; i++) {
                const currentPos = positions[i];
                const nextPos = positions[i + 1];
                const currentUnlocked = progress[i].is_unlocked || isAdmin;
                const nextUnlocked = progress[i + 1].is_unlocked || isAdmin;
                
                const line = document.createElement('div');
                line.className = `connection-line ${currentUnlocked && nextUnlocked ? 'unlocked' : ''}`;
                
                const x1 = currentPos.x + 37;
                const y1 = currentPos.y + 37;
                const x2 = nextPos.x + 37;
                const y2 = nextPos.y + 37;
                
                const length = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
                const angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
                
                line.style.left = `${x1}px`;
                line.style.top = `${y1}px`;
                line.style.width = `${length}px`;
                line.style.transform = `rotate(${angle}deg)`;
                
                container.appendChild(line);
            }
            
            progress.forEach((regionData, index) => {
                const region = regionData.region;
                const isUnlocked = regionData.is_unlocked || isAdmin;
                const isCompleted = regionData.completed_levels >= regionData.total_levels;
                const pos = positions[index];
                
                const node = document.createElement('div');
                node.className = `region-node ${isUnlocked ? 'unlocked' : 'locked'} ${isCompleted ? 'completed' : ''}`;
                node.style.left = `${pos.x}px`;
                node.style.top = `${pos.y}px`;
                
                if (isUnlocked) {
                    node.onclick = () => loadRegion(region.id);
                }
                
                const markerType = isCompleted ? 'completed' : (isUnlocked ? '' : 'locked');
                
                node.innerHTML = `
                    <div class="region-circle-wrapper">
                        <div class="region-ring"></div>
                        <div class="region-circle">${regionIcons[region.id] || '📍'}</div>
                        ${markerType ? `<div class="region-marker ${markerType}">${isCompleted ? '✓' : '🔒'}</div>` : ''}
                    </div>
                    <div class="region-label">${region.name}</div>
                    <div class="region-progress">
                        ${isCompleted ? '<span style="color:#00ff80">COMPLETE</span>' : 
                          (isUnlocked ? `${regionData.completed_levels}/${regionData.total_levels}` : 'LOCKED')}
                    </div>
                `;
                
                container.appendChild(node);
            });
        });
}

function loadRegion(regionId) {
    currentRegionId = regionId;
    
    fetch(`/api/region/${regionId}`)
        .then(response => response.json())
        .then(data => {
            const isCompleted = data.completed_quests.length === data.levels.length;
            const container = document.getElementById('regionContent');
            container.innerHTML = `
                <div class="region-header">
                    <div>
                        <h2>${data.region.name}</h2>
                        <p>${data.region.description}</p>
                    </div>
                    <button class="reset-btn" onclick="resetRegion('${regionId}')">
                        <i class="fas fa-rotate-right"></i> 重新挑战
                    </button>
                </div>
                <div class="mt-4">
                    ${data.levels.map((level, index) => {
                        const isCompleted = data.completed_quests.includes(level.id);
                        const isNext = !isCompleted && data.completed_quests.includes(data.levels[index - 1]?.id);
                        const isFirst = index === 0;
                        const isAccessible = isCompleted || isNext || isFirst || isAdmin;
                        
                        return `
                            <div class="level-card ${isCompleted ? 'completed' : (isAccessible ? 'current' : 'locked')}" 
                                 ${isAccessible ? `onclick="loadLevel('${regionId}', '${level.id}')"` : ''}
                                 style="cursor: ${isAccessible ? 'pointer' : 'not-allowed'}">
                                <div class="level-header">
                                    <span class="level-name">${level.name}</span>
                                    <span class="level-difficulty difficulty-${level.difficulty === '简单' ? 'easy' : level.difficulty === '中等' ? 'medium' : level.difficulty === '困难' ? 'hard' : 'extreme'}">
                                        ${level.difficulty}
                                    </span>
                                </div>
                                <p>${level.description}</p>
                                <div class="level-footer">
                                    <span>${isCompleted ? '✓ 已完成' : (isAccessible ? '点击开始' : '🔒 未解锁')}</span>
                                    <span class="text-yellow">经验: ${level.exp_reward} | 金币: ${level.gold_reward}</span>
                                </div>
                            </div>
                        `;
                    }).join('')}
                </div>
            `;
            
            switchSection('region-view');
        });
}

function resetRegion(regionId) {
    showModal('提示', '确定要重置这个区域吗？重置后可以重新挑战所有题目，但不会影响已解锁的章节和获得的金币。', function() {
        fetch(`/api/reset_region/${regionId}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                loadRegion(regionId);
            } else {
                showNotification(data.message, 'error');
            }
        })
        .catch(error => {
            showNotification('重置失败：' + error.message, 'error');
        });
    });
}

function openAvatarModal() {
    const modal = document.getElementById('avatarModal');
    const grid = document.getElementById('avatarGrid');
    
    fetch('/api/player')
        .then(response => response.json())
        .then(player => {
            const currentAvatar = player.avatar || '👤';
            
            grid.innerHTML = AVATARS.map(avatar => `
                <div class="avatar-item ${avatar === currentAvatar ? 'selected' : ''}" 
                     onclick="selectAvatar('${avatar}')">
                    ${avatar}
                </div>
            `).join('');
            
            modal.classList.remove('hidden');
        });
}

function closeAvatarModal() {
    document.getElementById('avatarModal').classList.add('hidden');
}

function selectAvatar(avatar) {
    fetch('/api/set_avatar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ avatar: avatar })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateAvatarDisplay(data.avatar);
            closeAvatarModal();
        }
    });
}

function handleAvatarUpload(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    const reader = new FileReader();
    reader.onload = function(e) {
        const image = new Image();
        image.onload = function() {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            const size = 128;
            canvas.width = size;
            canvas.height = size;
            
            const minDimension = Math.min(image.width, image.height);
            const x = (image.width - minDimension) / 2;
            const y = (image.height - minDimension) / 2;
            
            ctx.drawImage(image, x, y, minDimension, minDimension, 0, 0, size, size);
            
            const base64 = canvas.toDataURL('image/png');
            
            fetch('/api/set_avatar', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ avatar: base64 })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    updateAvatarDisplay(data.avatar);
                    closeAvatarModal();
                }
            });
        };
        image.src = e.target.result;
    };
    reader.readAsDataURL(file);
}

function updateAvatarDisplay(avatar) {
    currentPlayerAvatar = avatar;
    
    const avatarElements = document.querySelectorAll('.player-avatar, .player-avatar-sidebar, .chat-message.player .chat-avatar');
    avatarElements.forEach(el => {
        if (avatar.startsWith('data:image')) {
            el.innerHTML = `<img src="${avatar}" class="avatar-img" alt="头像">`;
        } else {
            el.innerHTML = avatar;
        }
    });
    
    const chatContainer = document.getElementById('levelContent');
    if (chatContainer) {
        const playerChatAvatars = chatContainer.querySelectorAll('.chat-message.player .chat-avatar');
        playerChatAvatars.forEach(el => {
            if (avatar.startsWith('data:image')) {
                el.innerHTML = `<img src="${avatar}" class="avatar-img" alt="头像">`;
            } else {
                el.innerHTML = avatar;
            }
        });
    }
}

function loadAdminSettings() {
    if (!isAdmin) {
        switchSection('world-map');
        return;
    }
    
    const container = document.getElementById('adminSettingsContainer');
    const isImageAvatar = npcAvatar.startsWith('data:image');
    container.innerHTML = `
        <div class="admin-settings-panel">
            <div class="settings-section">
                <h3><i class="fas fa-user-circle"></i> NPC 配置</h3>
                <div class="form-group">
                    <label>NPC 名称</label>
                    <input type="text" id="npcNameInput" value="${npcName}" class="form-control">
                </div>
                <div class="form-group">
                    <label>NPC 头像</label>
                    <div class="current-avatar-preview">
                        <span class="preview-label">当前头像：</span>
                        <span class="preview-avatar">${isImageAvatar ? `<img src="${npcAvatar}" class="avatar-img">` : npcAvatar}</span>
                    </div>
                    <div class="upload-section mb-3">
                        <label class="upload-btn">
                            <i class="fas fa-upload"></i> 上传自定义头像
                            <input type="file" id="npcAvatarUpload" accept="image/*" onchange="handleNpcAvatarUpload(event)" style="display: none;">
                        </label>
                    </div>
                    <div class="avatar-selector">
                        ${AVATARS.map(avatar => `
                            <div class="avatar-option ${!isImageAvatar && avatar === npcAvatar ? 'selected' : ''}" 
                                 onclick="selectNpcAvatar('${avatar}')">
                                ${avatar}
                            </div>
                        `).join('')}
                    </div>
                    <input type="hidden" id="npcAvatarInput" value="${npcAvatar}">
                </div>
                <button class="btn btn-success mt-4" onclick="saveNpcConfig()">
                    <i class="fas fa-save"></i> 保存设置
                </button>
            </div>
            
            <div class="settings-section">
                <div class="section-header">
                    <h3><i class="fas fa-users"></i> 玩家管理</h3>
                    <button class="btn btn-primary btn-sm" onclick="loadAdminPlayerList()">
                        <i class="fas fa-refresh"></i> 刷新列表
                    </button>
                </div>
                <div id="adminPlayerList"></div>
            </div>
        </div>
    `;
    
    loadAdminPlayerList();
}

function selectNpcAvatar(avatar) {
    document.getElementById('npcAvatarInput').value = avatar;
    document.querySelectorAll('.avatar-option').forEach(opt => opt.classList.remove('selected'));
    if (event) {
        event.target.classList.add('selected');
    }
}

function handleNpcAvatarUpload(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    const reader = new FileReader();
    reader.onload = function(e) {
        const image = new Image();
        image.onload = function() {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            const size = 128;
            canvas.width = size;
            canvas.height = size;
            
            const minDimension = Math.min(image.width, image.height);
            const x = (image.width - minDimension) / 2;
            const y = (image.height - minDimension) / 2;
            
            ctx.drawImage(image, x, y, minDimension, minDimension, 0, 0, size, size);
            
            const base64 = canvas.toDataURL('image/png');
            document.getElementById('npcAvatarInput').value = base64;
            
            const preview = document.querySelector('.preview-avatar');
            preview.innerHTML = `<img src="${base64}" class="avatar-img">`;
            
            document.querySelectorAll('.avatar-option').forEach(opt => opt.classList.remove('selected'));
        };
        image.src = e.target.result;
    };
    reader.readAsDataURL(file);
}

function saveNpcConfig() {
    const name = document.getElementById('npcNameInput').value.trim() || '富富';
    const avatar = document.getElementById('npcAvatarInput').value.trim() || '👩‍🏫';
    
    fetch('/api/npc_config', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, avatar })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            npcName = data.name;
            npcAvatar = data.avatar;
            alert('设置已保存！');
        } else {
            alert('保存失败：' + data.message);
        }
    });
}

function loadAdminPlayerList() {
    fetch('/api/leaderboard')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('adminPlayerList');
            
            if (!data.success || data.leaderboard.length === 0) {
                container.innerHTML = '<p class="text-muted text-center" style="padding: 20px;">暂无玩家数据</p>';
                return;
            }
            
            container.innerHTML = `<div class="admin-player-list">${data.leaderboard.map(player => {
                const isAdmin = player.name === '管理员';
                let avatarHtml = player.avatar && player.avatar.startsWith('data:image') 
                    ? `<img src="${player.avatar}" alt="${player.name}">` 
                    : (player.avatar || '👤');
                
                return `
                    <div class="admin-player-item ${isAdmin ? 'admin' : ''}">
                        <div class="admin-player-info">
                            <div class="admin-player-avatar">${avatarHtml}</div>
                            <div>
                                <div class="admin-player-name">${player.name}${isAdmin ? ' <span style="color:#FFD700;">(管理员)</span>' : ''}</div>
                                <div class="admin-player-stats">
                                    <span>Lv.${player.level}</span>
                                    <span>${player.gold} 金币</span>
                                    <span>${player.completed_quests} 题</span>
                                </div>
                            </div>
                        </div>
                        <div class="admin-player-actions">
                            ${isAdmin ? '' : `
                                <button class="btn btn-success btn-sm mr-2" onclick="addGoldToPlayer('${player.name}')">
                                    <i class="fas fa-coins"></i> 发放金币
                                </button>
                                <button class="btn btn-danger btn-sm" onclick="deletePlayer('${player.name}')">
                                    <i class="fas fa-trash"></i> 删除
                                </button>
                            `}
                        </div>
                    </div>
                `;
            }).join('')}</div>`;
        });
}

function addGoldToPlayer(playerName) {
    const amount = prompt(`请输入要给玩家 "${playerName}" 发放的金币数量：`, '100');
    if (amount === null) return;
    
    const goldAmount = parseInt(amount);
    if (isNaN(goldAmount) || goldAmount <= 0) {
        alert('请输入有效的金币数量（大于0）');
        return;
    }
    
    if (!confirm(`确定要给玩家 "${playerName}" 发放 ${goldAmount} 金币吗？`)) {
        return;
    }
    
    fetch('/api/admin/add_gold', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player_name: playerName, gold_amount: goldAmount })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            loadAdminPlayerList();
        } else {
            alert('操作失败：' + data.message);
        }
    })
    .catch(error => {
        alert('操作失败：' + error.message);
    });
}

function deletePlayer(playerName) {
    if (!confirm(`确定要删除玩家 "${playerName}" 的账号吗？此操作无法撤销！`)) {
        return;
    }
    
    fetch('/api/admin/delete_player', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player_name: playerName })
    })
    .then(response => response.json())
    .then(data => {
        showNotification(data.message, data.success ? 'success' : 'error');
        if (data.success) {
            loadAdminPlayerList();
        }
    });
}

function loadLevel(regionId, levelId) {
    currentRegionId = regionId;
    currentLevelId = levelId;
    
    Promise.all([
        fetch(`/api/level/${regionId}/${levelId}`),
        fetch('/api/player')
    ])
    .then(([levelRes, playerRes]) => Promise.all([levelRes.json(), playerRes.json()]))
    .then(([level, player]) => {
        const container = document.getElementById('levelContent');
        const revealCost = level.gold_reward + 5;
        
        const isImageAvatar = npcAvatar.startsWith('data:image');
        const avatarHtml = isImageAvatar ? `<img src="${npcAvatar}" class="avatar-img">` : npcAvatar;
        
        const playerAvatar = currentPlayerAvatar || player.avatar || '👤';
        const isPlayerImageAvatar = playerAvatar.startsWith('data:image');
        const playerAvatarHtml = isPlayerImageAvatar ? `<img src="${playerAvatar}" class="avatar-img">` : playerAvatar;
            
            let answerText = level.answer;
            if (level.type === 'choice' && level.options) {
                const correctOption = level.options.find(opt => {
                    const match = opt.match(/^([A-E])\.\s*/);
                    return match && match[1] === level.answer;
                });
                
                if (correctOption) {
                    const optionContent = correctOption.replace(/^[A-E]\.\s*/, '');
                    if (optionContent.includes('以上') || optionContent.includes('全部') || optionContent.includes('所有')) {
                        answerText = level.options.map(opt => opt.replace(/^[A-E]\.\s*/, '')).join('；');
                    } else {
                        answerText = optionContent;
                    }
                } else {
                    const letters = ['A', 'B', 'C', 'D', 'E'];
                    const answerIndex = letters.indexOf(level.answer);
                    if (answerIndex >= 0 && answerIndex < level.options.length) {
                        const optionContent = level.options[answerIndex].replace(/^[A-E]\.\s*/, '');
                        if (optionContent.includes('以上') || optionContent.includes('全部') || optionContent.includes('所有')) {
                            answerText = level.options.map(opt => opt.replace(/^[A-E]\.\s*/, '')).join('；');
                        } else {
                            answerText = optionContent;
                        }
                    }
                }
            }
            
            if (level.type === 'choice') {
                container.innerHTML = `
                    <div class="chat-container">
                        <div class="chat-header">
                            <h2>${level.name}</h2>
                            <span class="level-difficulty difficulty-${level.difficulty === '简单' ? 'easy' : level.difficulty === '中等' ? 'medium' : level.difficulty === '困难' ? 'hard' : 'extreme'}">
                                ${level.difficulty}
                            </span>
                        </div>
                        
                        <div class="chat-messages">
                            <div class="chat-message npc">
                                <div class="chat-avatar">${avatarHtml}</div>
                                <div class="chat-bubble">
                                    <div class="chat-name">${npcName}</div>
                                    <div class="chat-text">${level.question}</div>
                                </div>
                            </div>
                            
                            ${level.is_completed ? `
                                <div class="chat-message player">
                                    <div class="chat-bubble correct">
                                        <div class="chat-name">你</div>
                                        <div class="chat-text">${answerText}</div>
                                    </div>
                                    <div class="chat-avatar">${playerAvatarHtml}</div>
                                </div>
                                <div class="chat-message npc">
                                    <div class="chat-avatar">${avatarHtml}</div>
                                    <div class="chat-bubble success">
                                        <div class="chat-name">${npcName}</div>
                                        <div class="chat-text">✨ 回答正确！太棒了！</div>
                                    </div>
                                </div>
                            ` : ''}
                        </div>
                        
                        ${!level.is_completed ? `
                            <div class="chat-options">
                                ${level.options.map((opt, index) => {
                                    const letters = ['A', 'B', 'C', 'D', 'E'];
                                    const match = opt.match(/^([A-E])\.\s*/);
                                    const letter = match ? match[1] : letters[index];
                                    const text = match ? opt.replace(/^[A-E]\.\s*/, '') : opt;
                                    return `
                                        <div class="chat-option" onclick="submitChoice('${letter}')">
                                            <span class="option-letter">${letter}</span>
                                            <span class="option-text">${text}</span>
                                        </div>
                                    `;
                                }).join('')}
                            </div>
                        ` : ''}
                        
                        ${!level.is_completed ? `
                            <div class="chat-actions">
                                <button class="btn btn-warning" onclick="revealAnswer('${regionId}', '${levelId}')">
                                    <i class="fas fa-scroll"></i> 使用提示卷轴查看答案
                                </button>
                            </div>
                        ` : ''}
                    </div>
                    <div id="levelFeedback"></div>
                `;
            } else {
                container.innerHTML = `
                    <div class="chat-container">
                        <div class="chat-header">
                            <h2>${level.name}</h2>
                            <span class="level-difficulty difficulty-${level.difficulty === '简单' ? 'easy' : level.difficulty === '中等' ? 'medium' : level.difficulty === '困难' ? 'hard' : 'extreme'}">
                                ${level.difficulty}
                            </span>
                        </div>
                        
                        <div class="chat-messages">
                            <div class="chat-message npc">
                                <div class="chat-avatar">${avatarHtml}</div>
                                <div class="chat-bubble">
                                    <div class="chat-name">${npcName}</div>
                                    <div class="chat-text">${level.question}</div>
                                </div>
                            </div>
                            
                            ${level.is_completed ? `
                                <div class="chat-message player">
                                    <div class="chat-bubble correct">
                                        <div class="chat-name">你</div>
                                        <div class="chat-code">${level.answer}</div>
                                    </div>
                                    <div class="chat-avatar">${playerAvatarHtml}</div>
                                </div>
                                <div class="chat-message npc">
                                    <div class="chat-avatar">${avatarHtml}</div>
                                    <div class="chat-bubble success">
                                        <div class="chat-name">${npcName}</div>
                                        <div class="chat-text">✨ 代码运行成功！太棒了！</div>
                                    </div>
                                </div>
                            ` : ''}
                        </div>
                        
                        ${!level.is_completed && level.code_template ? `
                            <div class="code-hint">
                                <i class="fas fa-lightbulb"></i>
                                <span>提示：可以参考下面的模板</span>
                                <div class="code-template">${level.code_template.replace(/\n/g, '<br>')}</div>
                            </div>
                        ` : ''}
                        
                        ${!level.is_completed ? `
                            <div class="chat-input-area">
                                <textarea class="code-input" id="answerInput" placeholder="在此输入你的代码..."></textarea>
                                <button class="btn btn-success" onclick="submitAnswer()">
                                    <i class="fas fa-paper-plane"></i> 发送代码
                                </button>
                            </div>
                        ` : ''}
                        
                        ${!level.is_completed ? `
                            <div class="chat-actions">
                                <button class="btn btn-warning" onclick="revealAnswer('${regionId}', '${levelId}')">
                                    <i class="fas fa-scroll"></i> 使用提示卷轴查看答案
                                </button>
                            </div>
                        ` : ''}
                    </div>
                    <div id="levelFeedback"></div>
                `;
            }
            
            switchSection('level-view');
            
            if (level.type !== 'choice' && !level.is_completed) {
                setTimeout(() => {
                    setupCodeInput();
                }, 100);
            }
        });
}

let modalCallback = null;

function showModal(title, message, callback) {
    document.getElementById('modalTitle').textContent = title;
    document.getElementById('modalMessage').textContent = message;
    document.getElementById('customModal').classList.add('show');
    modalCallback = callback;
}

function showAnswerModal(title, answer) {
    document.getElementById('modalTitle').textContent = title;
    document.getElementById('modalMessage').innerHTML = '<div class="answer-content">' + answer + '</div>';
    document.getElementById('customModal').classList.add('show');
    modalCallback = null;
}

function closeModal() {
    document.getElementById('customModal').classList.remove('show');
    modalCallback = null;
}

function confirmModal() {
    if (modalCallback) {
        modalCallback();
    }
    closeModal();
}

document.addEventListener('DOMContentLoaded', function() {
    const customModal = document.getElementById('customModal');
    if (customModal) {
        customModal.addEventListener('click', function(e) {
            if (e.target === customModal) {
                closeModal();
            }
        });
    }
});

function revealAnswer(regionId, levelId) {
    showModal('提示', '确定要使用提示卷轴查看答案吗？', function() {
        fetch('/api/reveal_answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                region_id: regionId,
                level_id: levelId
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                showNotification(data.message);
                updatePlayer(data.player);
                
                const feedback = document.getElementById('levelFeedback');
                if (feedback) {
                    feedback.innerHTML = `
                        <div class="answer-reveal">
                            <div class="answer-header">
                                <i class="fas fa-lightbulb"></i>
                                <span>正确答案</span>
                            </div>
                            <div class="answer-code">${data.answer}</div>
                        </div>
                    `;
                }
            } else {
                showNotification(data.message, 'error');
            }
        })
        .catch(error => {
            showNotification('查看答案失败：' + error.message, 'error');
        });
    });
}

function selectChoice(idx) {
    const letters = ['A', 'B', 'C', 'D'];
    document.getElementById('answerInput').value = letters[idx] || '';
}

function submitChoice(answer) {
    if (!currentRegionId || !currentLevelId) {
        showNotification('无法获取当前关卡信息，请刷新页面', 'error');
        return;
    }
    
    console.log(`Submitting choice: region=${currentRegionId}, level=${currentLevelId}, answer=${answer}`);
    
    fetch('/api/submit_answer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            region_id: currentRegionId,
            level_id: currentLevelId,
            answer: answer
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const feedback = document.getElementById('levelFeedback');
        
        if (data.success) {
            feedback.innerHTML = `
                <div class="reward-box">
                    <h4>✓ 回答正确！</h4>
                    <div class="reward-item">
                        <i class="fas fa-star text-yellow"></i>
                        <span>获得 ${data.exp_reward} 经验值</span>
                    </div>
                    <div class="reward-item">
                        <i class="fas fa-coins text-yellow"></i>
                        <span>获得 ${data.gold_reward} 金币</span>
                    </div>
                    ${data.newly_unlocked && data.newly_unlocked.length > 0 ? `
                        <div class="mt-3">
                            <h5>🎉 解锁新成就！</h5>
                            ${data.newly_unlocked.map(ach => `
                                <div class="reward-item">
                                    <i class="fas fa-trophy text-yellow"></i>
                                    <span>${ach.name}: +${ach.reward} 金币</span>
                                </div>
                            `).join('')}
                        </div>
                    ` : ''}
                    ${data.all_completed && data.next_region ? `
                        <div class="mt-3">
                            <h5>🌟 新区域解锁！</h5>
                            <p>恭喜完成该区域所有关卡！</p>
                        </div>
                    ` : ''}
                </div>
            `;
            
            updatePlayer(data.player);
            
            if (data.newly_unlocked && data.newly_unlocked.length > 0) {
                setTimeout(() => {
                    showAchievementModal(data.newly_unlocked);
                }, 1000);
            }
            
            setTimeout(() => {
                if (data.all_completed && data.next_region) {
                    switchSection('world-map');
                } else {
                    fetch(`/api/region/${currentRegionId}`)
                        .then(r => r.json())
                        .then(regionData => {
                            const levels = regionData.levels;
                            const currentIndex = levels.findIndex(l => l.id === currentLevelId);
                            
                            if (currentIndex < levels.length - 1) {
                                loadLevel(currentRegionId, levels[currentIndex + 1].id);
                            } else {
                                loadRegion(currentRegionId);
                            }
                        });
                }
            }, 1500);
        } else {
            let damageHtml = '';
            const playerData = data.player;
            if (data.damage_info) {
                const dmg = data.damage_info;
                damageHtml = `
                    <div class="damage-info">
                        <div class="damage-breakdown">
                            <span class="damage-base">基础伤害: ${dmg.base_damage}</span>
                            <span class="damage-reduction">防御减免: -${dmg.defense_reduction}</span>
                            ${dmg.equipment_reduction > 0 ? `<span class="damage-reduction">装备减伤: -${dmg.equipment_reduction}</span>` : ''}
                            <span class="damage-final text-red">实际伤害: ${dmg.final_damage}</span>
                        </div>
                        <div class="hp-remaining">
                            <i class="fas fa-heart text-red"></i>
                            剩余生命: <span class="${dmg.remaining_hp < 30 ? 'text-red' : 'text-green'}">${dmg.remaining_hp}/${playerData ? playerData.max_hp : 100}</span>
                        </div>
                    </div>
                `;
                
                showDamageAnimation(dmg.final_damage);
            }
            
            feedback.innerHTML = `
                <div class="hint-box">
                    <i class="fas fa-exclamation-circle"></i>
                    <span>${data.message}</span>
                    ${damageHtml}
                    ${data.hint ? `<p>提示: ${data.hint}</p>` : ''}
                    ${data.damage_info && data.damage_info.remaining_hp <= 0 ? `
                        <div class="hp-zero-warning">
                            <i class="fas fa-skull-crossbones"></i>
                            <span>生命值耗尽！请购买生命药水恢复HP后再继续答题</span>
                        </div>
                    ` : ''}
                </div>
            `;
            
            if (data.player) {
                updatePlayer(data.player);
            }
        }
    })
    .catch(error => {
        console.error('Submit choice error:', error);
        showNotification('提交答案失败，请重试', 'error');
    });
}

function setupCodeInput() {
    const textarea = document.getElementById('answerInput');
    if (textarea && textarea.tagName === 'TEXTAREA') {
        textarea.addEventListener('keydown', function(e) {
            if (e.key === 'Tab') {
                e.preventDefault();
                
                const start = this.selectionStart;
                const end = this.selectionEnd;
                const value = this.value;
                const spaces = '    ';
                
                this.value = value.substring(0, start) + spaces + value.substring(end);
                
                this.selectionStart = this.selectionEnd = start + 4;
            }
            
            if (e.key === 'Enter') {
                e.preventDefault();
                
                const start = this.selectionStart;
                const end = this.selectionEnd;
                const value = this.value;
                
                const lineStart = value.lastIndexOf('\n', start - 1);
                const lineContent = value.substring(lineStart + 1, start);
                const match = lineContent.match(/^\s*/);
                let indent = match ? match[0] : '';
                
                indent = indent.replace(/\t/g, '    ');
                
                this.value = value.substring(0, start) + '\n' + indent + value.substring(end);
                
                this.selectionStart = this.selectionEnd = start + 1 + indent.length;
            }
            
            if (e.key === 'Backspace') {
                const start = this.selectionStart;
                const value = this.value;
                
                if (start > 0 && value.substring(start - 4, start) === '    ') {
                    e.preventDefault();
                    this.value = value.substring(0, start - 4) + value.substring(start);
                    this.selectionStart = this.selectionEnd = start - 4;
                }
            }
        });
    }
}

function submitAnswer() {
    const answerInput = document.getElementById('answerInput');
    if (!answerInput) {
        showNotification('无法找到答案输入框', 'error');
        return;
    }
    
    const answer = answerInput.value;
    
    if (!currentRegionId || !currentLevelId) {
        showNotification('无法获取当前关卡信息，请刷新页面', 'error');
        return;
    }
    
    fetch('/api/submit_answer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            region_id: currentRegionId,
            level_id: currentLevelId,
            answer: answer
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        const feedback = document.getElementById('levelFeedback');
        
        if (data.success) {
            feedback.innerHTML = `
                <div class="reward-box">
                    <h4>✓ 回答正确！</h4>
                    <div class="reward-item">
                        <i class="fas fa-star text-yellow"></i>
                        <span>获得 ${data.exp_reward} 经验值</span>
                    </div>
                    <div class="reward-item">
                        <i class="fas fa-coins text-yellow"></i>
                        <span>获得 ${data.gold_reward} 金币</span>
                    </div>
                    ${data.newly_unlocked && data.newly_unlocked.length > 0 ? `
                        <div class="mt-3">
                            <h5>🎉 解锁新成就！</h5>
                            ${data.newly_unlocked.map(ach => `
                                <div class="reward-item">
                                    <i class="fas fa-trophy text-yellow"></i>
                                    <span>${ach.name}: +${ach.reward} 金币</span>
                                </div>
                            `).join('')}
                        </div>
                    ` : ''}
                    ${data.all_completed && data.next_region ? `
                        <div class="mt-3">
                            <h5>🌟 新区域解锁！</h5>
                            <p>恭喜完成该区域所有关卡！</p>
                        </div>
                    ` : ''}
                </div>
            `;
            
            updatePlayer(data.player);
            
            setTimeout(() => {
                if (data.all_completed && data.next_region) {
                    switchSection('world-map');
                } else {
                    fetch(`/api/region/${currentRegionId}`)
                        .then(r => r.json())
                        .then(regionData => {
                            const levels = regionData.levels;
                            const currentIndex = levels.findIndex(l => l.id === currentLevelId);
                            
                            if (currentIndex < levels.length - 1) {
                                loadLevel(currentRegionId, levels[currentIndex + 1].id);
                            } else {
                                loadRegion(currentRegionId);
                            }
                        });
                }
            }, 1500);
        } else {
            // 显示答错反馈和HP变化
            let damageHtml = '';
            const playerData = data.player;
            if (data.damage_info) {
                const dmg = data.damage_info;
                damageHtml = `
                    <div class="damage-info">
                        <div class="damage-breakdown">
                            <span class="damage-base">基础伤害: ${dmg.base_damage}</span>
                            <span class="damage-reduction">防御减免: -${dmg.defense_reduction}</span>
                            ${dmg.equipment_reduction > 0 ? `<span class="damage-reduction">装备减伤: -${dmg.equipment_reduction}</span>` : ''}
                            <span class="damage-final text-red">实际伤害: ${dmg.final_damage}</span>
                        </div>
                        <div class="hp-remaining">
                            <i class="fas fa-heart text-red"></i>
                            剩余生命: <span class="${dmg.remaining_hp < 30 ? 'text-red' : 'text-green'}">${dmg.remaining_hp}/${playerData ? playerData.max_hp : 100}</span>
                        </div>
                    </div>
                `;
                
                // 显示扣血动画
                showDamageAnimation(dmg.final_damage);
            }
            
            feedback.innerHTML = `
                <div class="hint-box">
                    <i class="fas fa-exclamation-circle"></i>
                    <span>${data.message}</span>
                    ${damageHtml}
                    ${data.hint ? `<p>提示: ${data.hint}</p>` : ''}
                    ${data.damage_info && data.damage_info.remaining_hp <= 0 ? `
                        <div class="hp-zero-warning">
                            <i class="fas fa-skull-crossbones"></i>
                            <span>生命值耗尽！请购买生命药水恢复HP后再继续答题</span>
                        </div>
                    ` : ''}
                </div>
            `;
            
            if (data.player) {
                updatePlayer(data.player);
            }
        }
    })
    .catch(error => {
        console.error('Submit answer error:', error);
        showNotification('提交答案失败，请重试', 'error');
    });
}

function updatePlayer(playerData) {
    if (!playerData) {
        console.warn('updatePlayer called with null/undefined player data');
        return;
    }
    
    document.getElementById('playerGold').textContent = playerData.gold;
    
    const scrollCount = playerData.inventory ? playerData.inventory.filter(item => item.id === 'hint_scroll').length : 0;
    const scrollEl = document.getElementById('playerScrolls');
    if (scrollEl) {
        scrollEl.textContent = scrollCount;
    }
    
    const levelBar = document.querySelector('.progress-bar');
    const expPercent = (playerData.exp / getExpNeeded(playerData.level)) * 100;
    levelBar.style.width = `${expPercent}%`;
    
    document.querySelector('.level-bar span:first-child').textContent = `等级 ${playerData.level}`;
    document.querySelector('.level-bar span:last-child').textContent = `${playerData.exp}/${getExpNeeded(playerData.level)}`;
    
    document.querySelectorAll('.stat-value')[0].textContent = `${playerData.hp}/${playerData.max_hp}`;
    document.querySelectorAll('.stat-value')[1].textContent = playerData.attack;
    document.querySelectorAll('.stat-value')[2].textContent = playerData.defense;
    
    const equipmentSlots = document.querySelector('.equipment-slots');
    if (equipmentSlots && playerData.equipment) {
        const items = Object.values(playerData.equipment);
        if (items.length > 0) {
            const iconMap = {
                'wisdom_hat': 'fa-graduation-cap',
                'gold_ring': 'fa-ring',
                'iron_armor': 'fa-shield-alt'
            };
            equipmentSlots.innerHTML = items.map(item => {
                const icon = iconMap[item.id] || 'fa-question';
                return `
                    <div class="slot has-tooltip" title="${item.name}: ${item.description}">
                        <i class="fas ${icon}"></i>
                    </div>
                `;
            }).join('');
        } else {
            equipmentSlots.innerHTML = '';
        }
    }
    
    let consumablesArea = document.querySelector('.consumables');
    if (!consumablesArea) {
        const equipmentDiv = document.querySelector('.equipment');
        if (equipmentDiv) {
            consumablesArea = document.createElement('div');
            consumablesArea.className = 'consumables mt-4';
            equipmentDiv.appendChild(consumablesArea);
        }
    }
    if (consumablesArea) {
        if (scrollCount > 0) {
            consumablesArea.innerHTML = `
                <h4><i class="fas fa-scroll"></i> 消耗品</h4>
                <div class="consumable-slots">
                    <div class="slot has-tooltip" title="提示卷轴: 查看答案时消耗一个，剩余 ${scrollCount} 个">
                        <i class="fas fa-scroll"></i>
                        <span class="slot-count">×${scrollCount}</span>
                    </div>
                </div>
            `;
        } else {
            consumablesArea.innerHTML = '';
        }
    }
    
    isAdmin = playerData.is_admin || false;
    
    if (playerData.avatar) {
        updateAvatarDisplay(playerData.avatar);
    }
}

function getExpNeeded(level) {
    return Math.floor(100 * Math.pow(1.5, level - 1));
}

function loadQuests() {
    fetch('/api/quests')
        .then(response => response.json())
        .then(quests => {
            const container = document.getElementById('questsContainer');
            
            if (quests.length === 0) {
                container.innerHTML = '<p class="text-muted">暂无活跃任务</p>';
                return;
            }
            
            container.innerHTML = quests.map(q => {
                const quest = q.quest;
                const progress = q.progress;
                const progressPercent = (progress.current / progress.total) * 100;
                const isComplete = progress.current >= progress.total;
                
                return `
                    <div class="quest-card">
                        <h4>${quest.name}</h4>
                        <p>${quest.description}</p>
                        <div class="quest-progress">
                            <div class="d-flex justify-content-between mb-1">
                                <span>进度</span>
                                <span>${progress.current}/${progress.total}</span>
                            </div>
                            <div class="progress-bar-quest">
                                <div class="progress-fill" style="width: ${progressPercent}%"></div>
                            </div>
                        </div>
                        <div class="mt-2">
                            <span class="text-yellow">奖励: ${quest.exp_reward} 经验, ${quest.gold_reward} 金币</span>
                        </div>
                        ${isComplete ? `
                            <button class="btn btn-success mt-3" onclick="completeQuest('${quest.id}')">
                                <i class="fas fa-check"></i> 领取奖励
                            </button>
                        ` : ''}
                    </div>
                `;
            }).join('');
        });
}

function completeQuest(questId) {
    fetch('/api/complete_quest', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ quest_id: questId })
    })
    .then(response => response.json())
    .then(data => {
        showNotification(data.message);
        
        if (data.success) {
            updatePlayer(data.player);
            loadQuests();
        }
    });
}

function loadShop() {
    fetch('/api/shop')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('shopContainer');
            
            container.innerHTML = `
                <div class="mb-4">
                    <span class="text-yellow">你的金币: ${data.player_gold}</span>
                </div>
                <h4>消耗品</h4>
                ${data.items.filter(i => i.type === 'consumable').map(item => `
                    <div class="shop-item">
                        <div class="shop-item-header">
                            <span class="shop-item-name">${item.name}</span>
                            <span class="shop-item-price">${item.price} 金币</span>
                        </div>
                        <div class="shop-item-description">${item.description}</div>
                        <button class="btn btn-success mt-2" onclick="buyItem('${item.id}')">
                            <i class="fas fa-shopping-cart"></i> 购买
                        </button>
                    </div>
                `).join('')}
                <h4 class="mt-6">装备</h4>
                ${data.items.filter(i => i.type === 'equipment').map(item => {
                    const canBuy = data.player_gold >= item.price;
                    return `
                        <div class="shop-item">
                            <div class="shop-item-header">
                                <span class="shop-item-name">${item.name}</span>
                                <span class="shop-item-price ${!canBuy ? 'text-red' : ''}">${item.price} 金币</span>
                            </div>
                            <div class="shop-item-description">${item.description}</div>
                            ${item.stats ? `
                                <div class="shop-item-stats">
                                    ${Object.entries(item.stats).map(([stat, val]) => `
                                        <span class="stat-badge">${stat}: +${val}</span>
                                    `).join('')}
                                </div>
                            ` : ''}
                            <button class="btn ${canBuy ? 'btn-success' : 'btn-secondary disabled'} mt-2" onclick="buyItem('${item.id}')" ${!canBuy ? 'disabled' : ''}>
                                <i class="fas fa-shopping-cart"></i> 购买
                            </button>
                        </div>
                    `;
                }).join('')}
            `;
        });
}

function buyItem(itemId) {
    fetch('/api/buy_item', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ item_id: itemId })
    })
    .then(response => response.json())
    .then(data => {
        showNotification(data.message);
        
        if (data.success) {
            updatePlayer(data.player);
            loadShop();
        }
    });
}

function loadAchievements() {
    fetch('/api/achievements')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('achievementsContainer');
            
            container.innerHTML = data.achievements.map(ach => {
                const isUnlocked = data.unlocked.includes(ach.id);
                
                return `
                    <div class="achievement-card ${isUnlocked ? 'unlocked' : 'locked'}">
                        <div class="achievement-icon">
                            ${isUnlocked ? '🏆' : '🔒'}
                        </div>
                        <div class="achievement-info">
                            <h4>${ach.name}</h4>
                            <p>${ach.description}</p>
                            <span class="text-yellow">奖励: ${ach.reward} 金币</span>
                        </div>
                        ${isUnlocked ? '<span class="text-green">✓ 已解锁</span>' : ''}
                    </div>
                `;
            }).join('');
        });
}

function loadLeaderboard() {
    fetch('/api/leaderboard')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('leaderboardContainer');
            
            if (!data.success || data.leaderboard.length === 0) {
                container.innerHTML = '<p class="text-muted text-center" style="padding: 40px;">暂无玩家数据</p>';
                return;
            }
            
            container.innerHTML = `<div class="leaderboard-container">${data.leaderboard.map((player, index) => {
                const rankClass = index === 0 ? 'top-1' : (index === 1 ? 'top-2' : (index === 2 ? 'top-3' : 'other'));
                const rankNum = index + 1;
                
                let avatarHtml = player.avatar && player.avatar.startsWith('data:image') 
                    ? `<img src="${player.avatar}" alt="${player.name}">` 
                    : (player.avatar || '👤');
                
                return `
                    <div class="leaderboard-item ${rankClass}">
                        <div class="leaderboard-rank ${rankClass}">${rankNum}</div>
                        <div class="leaderboard-avatar">${avatarHtml}</div>
                        <div class="leaderboard-info">
                            <div class="leaderboard-name">${player.name}</div>
                            <div class="leaderboard-stats">
                                <span><i class="fas fa-coins"></i> ${player.gold}</span>
                                <span><i class="fas fa-check-circle"></i> ${player.completed_quests} 题</span>
                                <span><i class="fas fa-map"></i> ${player.unlocked_regions} 区域</span>
                            </div>
                        </div>
                        <div class="leaderboard-level">
                            <div class="leaderboard-level-number">Lv.${player.level}</div>
                            <div class="leaderboard-level-label">经验 ${player.exp}</div>
                        </div>
                    </div>
                `;
            }).join('')}</div>`;
        });
}

function backToWorldMap() {
    switchSection('world-map');
}

function backToRegion() {
    if (currentRegionId) {
        loadRegion(currentRegionId);
    } else {
        switchSection('world-map');
    }
}

function saveGame() {
    fetch('/api/save_game')
        .then(response => response.json())
        .then(data => {
            showNotification(data.message);
        });
}

function autoSaveGame() {
    fetch('/api/save_game')
        .then(response => response.json())
        .then(data => {
            console.log('自动保存:', data.message);
        });
}

document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('beforeunload', function() {
        autoSaveGame();
    });
    
    setInterval(autoSaveGame, 30000);
});

function confirmReset() {
    if (confirm('确定要返回主菜单吗？当前进度将自动保存。')) {
        saveGame();
        setTimeout(() => {
            window.location.href = '/';
        }, 500);
    }
}

function showDamageAnimation(damage) {
    // 创建扣血动画元素
    const damageOverlay = document.createElement('div');
    damageOverlay.className = 'damage-overlay';
    damageOverlay.innerHTML = `
        <div class="damage-number">
            <i class="fas fa-heart-crack"></i>
            -${damage}
        </div>
    `;
    
    // 添加到页面
    document.body.appendChild(damageOverlay);
    
    // 3秒后移除
    setTimeout(() => {
        damageOverlay.remove();
    }, 3000);
}

function showNotification(message, type = 'info') {
    const notification = document.getElementById('notification');
    const notificationMessage = document.getElementById('notificationMessage');
    
    notificationMessage.textContent = message;
    notification.classList.remove('hidden');
    
    setTimeout(() => {
        notification.classList.add('hidden');
    }, 3000);
}