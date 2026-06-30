let currentRegionId = null;
let currentLevelId = null;
let isAdmin = false;

document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/player')
        .then(response => response.json())
        .then(playerData => {
            isAdmin = playerData.is_admin || false;
            console.log('Player loaded, isAdmin:', isAdmin);
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
    } else if (sectionId === 'inventory') {
        loadInventory();
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
                'day20': '💎',
                'day21': '💀'
            };
            
            progress.forEach((regionData, index) => {
                const region = regionData.region;
                const isUnlocked = regionData.is_unlocked || isAdmin;
                
                console.log(`Region ${index}: id=${region.id}, name=${region.name}, is_unlocked=${isUnlocked}, type=${typeof isUnlocked}`);
                
                const card = document.createElement('div');
                card.className = `region-card ${isUnlocked ? 'unlocked' : 'locked'}`;
                
                if (isUnlocked) {
                    card.onclick = () => loadRegion(region.id);
                    card.style.cursor = 'pointer';
                }
                
                card.innerHTML = `
                    <div class="region-icon">${regionIcons[region.id] || '📍'}</div>
                    <div class="region-name">${region.name}</div>
                    <div class="region-status">
                        ${isAdmin ? '<span class="text-yellow">[管理员]</span>' : 
                          (regionData.is_unlocked 
                            ? `<span class="text-green">已解锁</span> (${regionData.completed_levels}/${regionData.total_levels})` 
                            : '<span class="text-red">未解锁</span>')}
                    </div>
                    <div style="font-size: 0.85rem; color: #BDBDBD; margin-top: 0.5rem;">
                        ${region.description}
                    </div>
                `;
                
                container.appendChild(card);
            });
        });
}

function loadRegion(regionId) {
    currentRegionId = regionId;
    
    fetch(`/api/region/${regionId}`)
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('regionContent');
            container.innerHTML = `
                <h2>${data.region.name}</h2>
                <p>${data.region.description}</p>
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

function loadLevel(regionId, levelId) {
    currentRegionId = regionId;
    currentLevelId = levelId;
    
    fetch(`/api/level/${regionId}/${levelId}`)
        .then(response => response.json())
        .then(level => {
            const container = document.getElementById('levelContent');
            const revealCost = level.gold_reward + 5;
            
            if (level.type === 'choice') {
                container.innerHTML = `
                    <h2>${level.name}</h2>
                    ${level.is_completed ? `
                        <div class="alert alert-success mt-4">
                            <i class="fas fa-check-circle"></i> 已完成 | 正确答案: ${level.answer}
                        </div>
                    ` : ''}
                    <div class="mt-4">
                        <p class="question-text">${level.question}</p>
                    </div>
                    <div class="mt-4 options-list">
                        ${level.options.map((opt, index) => {
                            const letters = ['A', 'B', 'C', 'D', 'E'];
                            const match = opt.match(/^([A-E])\.\s*/);
                            const letter = match ? match[1] : letters[index];
                            const text = match ? opt.replace(/^[A-E]\.\s*/, '') : opt;
                            const isCorrect = level.is_completed && letter === level.answer;
                            return `
                                <div class="option-card ${isCorrect ? 'correct' : ''}" ${level.is_completed ? '' : `onclick="submitChoice('${letter}')"`}>
                                    <span class="option-letter">${letter}</span>
                                    <span class="option-text">${text}</span>
                                </div>
                            `;
                        }).join('')}
                    </div>
                    ${!level.is_completed ? `
                        <div class="mt-4">
                            <button class="btn btn-warning" onclick="revealAnswer('${regionId}', '${levelId}', ${revealCost})">
                                <i class="fas fa-eye"></i> 花费 ${revealCost} 金币查看答案
                            </button>
                        </div>
                    ` : ''}
                    <div id="levelFeedback"></div>
                `;
            } else {
                container.innerHTML = `
                    <h2>${level.name}</h2>
                    <div class="level-info">
                        <span class="level-difficulty difficulty-${level.difficulty === '简单' ? 'easy' : level.difficulty === '中等' ? 'medium' : level.difficulty === '困难' ? 'hard' : 'extreme'}">
                            ${level.difficulty}
                        </span>
                        <span class="text-yellow">经验: ${level.exp_reward} | 金币: ${level.gold_reward}</span>
                    </div>
                    <div class="mt-4">
                        <h4>问题</h4>
                        <p>${level.question}</p>
                    </div>
                    ${level.is_completed ? `
                        <div class="mt-4 alert alert-success">
                            <i class="fas fa-check-circle"></i> 已完成 | 正确答案:
                            <pre class="mt-2">${level.answer}</pre>
                        </div>
                    ` : ''}
                    ${!level.is_completed && level.code_template ? `
                        <div class="mt-4">
                            <h4>代码模板</h4>
                            <div class="code-template">${level.code_template.replace(/\n/g, '<br>')}</div>
                        </div>
                    ` : ''}
                    ${!level.is_completed ? `
                        <div class="mt-4 level-form">
                            <textarea class="code-input" id="answerInput" placeholder="在此输入你的代码..."></textarea>
                            <button class="btn btn-success mt-3" onclick="submitAnswer()">
                                <i class="fas fa-check"></i> 提交答案
                            </button>
                        </div>
                    ` : ''}
                    ${!level.is_completed ? `
                        <div class="mt-4">
                            <button class="btn btn-warning" onclick="revealAnswer('${regionId}', '${levelId}', ${revealCost})">
                                <i class="fas fa-eye"></i> 花费 ${revealCost} 金币查看答案
                            </button>
                        </div>
                    ` : ''}
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

function revealAnswer(regionId, levelId, cost) {
    if (!confirm(`确定要花费 ${cost} 金币查看答案吗？`)) {
        return;
    }
    
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
            feedback.innerHTML = `
                <div class="alert alert-info mt-4">
                    <i class="fas fa-lightbulb"></i> 正确答案:
                    <pre class="mt-2">${data.answer}</pre>
                </div>
            `;
        } else {
            showNotification(data.message, 'error');
        }
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
            
            setTimeout(() => {
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
            }, 2000);
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
                loadRegion(currentRegionId);
            }, 3000);
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
    
    const levelBar = document.querySelector('.progress-bar');
    const expPercent = (playerData.exp / getExpNeeded(playerData.level)) * 100;
    levelBar.style.width = `${expPercent}%`;
    
    document.querySelector('.level-bar span:first-child').textContent = `等级 ${playerData.level}`;
    document.querySelector('.level-bar span:last-child').textContent = `${playerData.exp}/${getExpNeeded(playerData.level)}`;
    
    document.querySelectorAll('.stat-value')[0].textContent = `${playerData.hp}/${playerData.max_hp}`;
    document.querySelectorAll('.stat-value')[1].textContent = playerData.attack;
    document.querySelectorAll('.stat-value')[2].textContent = playerData.defense;
    
    isAdmin = playerData.is_admin || false;
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

function loadInventory() {
    fetch('/api/inventory')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('inventoryContainer');
            
            if (data.inventory.length === 0) {
                container.innerHTML = '<p class="text-muted">背包是空的</p>';
            } else {
                container.innerHTML = data.inventory.map(item => `
                    <div class="inventory-item">
                        <div>
                            <span class="inventory-item-name">${item.name}</span>
                            <p class="text-muted" style="font-size: 0.85rem;">${item.description}</p>
                        </div>
                        <div class="inventory-item-actions">
                            ${item.type === 'equipment' ? `
                                <button class="btn btn-warning btn-sm" onclick="equipItem('${item.id}')">
                                    <i class="fas fa-shield"></i> 装备
                                </button>
                            ` : `
                                <button class="btn btn-success btn-sm" onclick="useItem('${item.id}')">
                                    <i class="fas fa-flask"></i> 使用
                                </button>
                            `}
                        </div>
                    </div>
                `).join('');
            }
            
            if (Object.keys(data.equipment).length > 0) {
                container.innerHTML += `
                    <h4 class="mt-6">已装备</h4>
                    ${Object.entries(data.equipment).map(([slot, item]) => `
                        <div class="inventory-item">
                            <div>
                                <span class="text-muted">${slot}</span>
                                <span class="inventory-item-name">${item.name}</span>
                            </div>
                        </div>
                    `).join('')}
                `;
            }
        });
}

function equipItem(itemId) {
    fetch('/api/equip_item', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ item_id: itemId })
    })
    .then(response => response.json())
    .then(data => {
        showNotification(data.message);
        
        if (data.success) {
            updatePlayer(data.player);
            loadInventory();
        }
    });
}

function useItem(itemId) {
    fetch('/api/use_item', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ item_id: itemId })
    })
    .then(response => response.json())
    .then(data => {
        showNotification(data.message);
        
        if (data.success) {
            updatePlayer(data.player);
            loadInventory();
        }
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